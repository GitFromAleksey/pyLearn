import re


text_list = []
text_list.append(r'[FLTR1]cz_task: czidx=1, czid=860049889, numTH=1: T=25.61, H=22.7, numCO2=1: CO2=526.0, TMCU=53.71, TMB=39.88, numPM=0, pm1p0=65535, pm2p5=65535, pm10=65535')
text_list.append(r'upd: sm=0, idle, DT=0x0000, MAC-0a:34:56:78:9A:BC, prg=0%')
text_list.append(r'[EVT]: BLE_GAP_EVT_CONNECTED')
text_list.append(r'__clndr_check_md5: CLNDR MD5 compare OK')
text_list.append(r'__TB3_check_CZ_mode_and_set_auto: err Tion B4 connect')
text_list.append(r'__TB3_check_CZ_mode_and_set_auto: err Tion B3 connect')
text_list.append(r'__TB3_check_CZ_mode_and_set_auto: err Tion O2 RF connect')
text_list.append(r'beacon_RX: 14124434, COORD_ID MAC: s, RSSI=32')
text_list.append(r'BleCentralManualConnectStart: start con for 84:DF:A4:25:B5:FC')
text_list.append(r'DevFileOp: st=idle, sID=0, dst=idleMAC-00:00:00:00:00:00, type=0, prg=0%')
text_list.append(r'recv frame: 0x2e02, ID=2530')
text_list.append(r'RfCheckDevState: ERR CHECK DEV STATE FOR 0x1007, mac-BA:F7:10:4E:4A:68 errc=200')
text_list.append(r'wifi_scan_net: new try scan...')
text_list.append(r'wifi_scan_net: geneticunifi, rssi=-70, SecType=3, BSID-24:A4:3C:4D:0D:17')
text_list.append(r'wifi_scan_net: Keenetic-7363, rssi=-74, SecType=3, BSID-50:FF:20:0E:D8:76')
text_list.append(r'wifi_scan_net: duplicate entry')
text_list.append(r'wifi_scan_net: disable scan')
text_list.append(r'wifi_scan_net: DIRECT-56-HP M426 LaserJet, rssi=-75, SecType=3, BSID-9E:30:5B:8E:8B:56')
text_list.append(r'wifi_scan_net: TION-guest, rssi=-59, SecType=0, BSID-FE:92:BF:CA:F1:D1')
text_list.append(r'wifi_sync_cur_state: Sync OK, ID=0, pck_size=956, ping 209')
text_list.append(r'wifi_send_frame_ok: send OK OK')


class cValuePattern:
    VALUE_NAME      = 'VALUE_NAME'
    VALUE_SEPARATOR = 'VALUE_SEPARATOR'
    VALUE_PATTERN   = 'VALUE_PATTERN'
    VALUE_END       = 'VALUE_END'
    
    def __init__(self, v_name, v_sep, v_patt, v_end):
        k_name   = cValuePattern.VALUE_NAME
        k_separ  = cValuePattern.VALUE_SEPARATOR
        k_v_patt = cValuePattern.VALUE_PATTERN
        k_end    = cValuePattern.VALUE_END
        self.pattern = {}
        self.pattern[k_name]   = v_name
        self.pattern[k_separ]  = v_sep
        self.pattern[k_v_patt] = v_patt
        self.pattern[k_end]    = v_end
        self.re_patt = self.pattern[k_name] + self.pattern[k_separ] + self.pattern[k_v_patt] + self.pattern[k_end]

    def GetName(self):
        return self.pattern[cValuePattern.VALUE_NAME]

    def GetRePattern(self):
        return self.re_patt

    def Parse(self, text):
        find = re.search(self.re_patt, text)
        if find:
            name = re.search(self.pattern[cValuePattern.VALUE_NAME], find.group()).group()
            value = re.split(self.pattern[cValuePattern.VALUE_SEPARATOR], find.group())[1]
            value = re.search(self.pattern[cValuePattern.VALUE_PATTERN], value).group()
            return {name: value}
        return None
                

class cTegPattern():
    TEG = 'TEG'
    PATTERN = 'PATTERNS'
    
    def __init__(self, teg):
        self.teg = cValuePattern(teg, r'',r'',r'')
        self.patterns = []

    def AddValuePattern(self, v_patt):
        self.patterns.append(v_patt)

    def AddValuePatterns(self, v_patts):
        self.patterns = self.patterns + v_patts

    def Parse(self, text):
        res = {}
        v_res = {}
        find = self.teg.Parse(text)
        if find:
            for v_pat in self.patterns:
                val = v_pat.Parse(text)
                if val:
                    v_res.update(val)
            res[self.teg.GetName()] = v_res
        else:
            res = None
        return res

class cMaParser():
    
    def __init__(self):
        self.teg_patterns = []#cTegPattern

    def AddTegPattern(self, teg_patt):
        self.teg_patterns.append(teg_patt)

    def Parse(self, text):
        res = []
        for teg in self.teg_patterns:
            pars_res = teg.Parse(text)
            if pars_res:
                return pars_res
        return None


RE_PATT_MAC = r'([\dA-Fa-f]{2}:){5}[\dA-Fa-f]{2}'
RE_PATT_ONE_DIGIT = r'\d'
RE_PATT_MULT_DIGITS = r'\d+'
RE_PATT_HEX_DIGIT = r'\dx[a-fA-F\d]+'#r'\dx\d+'
RE_PATT_FLOAT_DIGIT = r'\d+.\d+'


def main():
    global TEG
    global PATTERN
    global filtr1_ptrns
    
    parser = cMaParser()

    teg_patt = cTegPattern(r'upd:')
    teg_patt.AddValuePattern(cValuePattern(r'sm',   r'=', RE_PATT_ONE_DIGIT,   r','))
    teg_patt.AddValuePattern(cValuePattern(r'idle', r'',  r'',                 r','))
    teg_patt.AddValuePattern(cValuePattern(r'DT',   r'=', RE_PATT_HEX_DIGIT,   r','))
    teg_patt.AddValuePattern(cValuePattern(r'MAC',  r'-', RE_PATT_MAC,         r','))
    teg_patt.AddValuePattern(cValuePattern(r'prg',  r'=', RE_PATT_MULT_DIGITS, r'%'))
    parser.AddTegPattern(teg_patt)

    teg_patt = cTegPattern(r'\[FLTR1\]cz_task:')
    teg_patt.AddValuePattern(cValuePattern(r'czidx',  r'=' , RE_PATT_ONE_DIGIT,   r','))
    teg_patt.AddValuePattern(cValuePattern(r'czid',   r'=' , RE_PATT_MULT_DIGITS, r','))
    teg_patt.AddValuePattern(cValuePattern(r'numTH',  r'=' , RE_PATT_MULT_DIGITS, r':'))
    teg_patt.AddValuePattern(cValuePattern(r'T',      r'=' , RE_PATT_FLOAT_DIGIT, r','))
    teg_patt.AddValuePattern(cValuePattern(r'H',      r'=' , RE_PATT_FLOAT_DIGIT, r','))
    teg_patt.AddValuePattern(cValuePattern(r'numCO2', r'=' , RE_PATT_ONE_DIGIT,   r':'))
    teg_patt.AddValuePattern(cValuePattern(r'CO2',    r'=' , RE_PATT_FLOAT_DIGIT, r','))
    teg_patt.AddValuePattern(cValuePattern(r'TMCU',   r'=' , RE_PATT_FLOAT_DIGIT, r','))
    teg_patt.AddValuePattern(cValuePattern(r'TMB',    r'=' , RE_PATT_FLOAT_DIGIT, r','))
    teg_patt.AddValuePattern(cValuePattern(r'numPM',  r'=' , RE_PATT_ONE_DIGIT,   r','))
    teg_patt.AddValuePattern(cValuePattern(r'pm1p0',  r'=' , RE_PATT_MULT_DIGITS, r','))
    teg_patt.AddValuePattern(cValuePattern(r'pm2p5',  r'=' , RE_PATT_MULT_DIGITS, r','))
    teg_patt.AddValuePattern(cValuePattern(r'pm10',   r'=' , RE_PATT_MULT_DIGITS, r''))
    parser.AddTegPattern(teg_patt)

##'[EVT]: BLE_GAP_EVT_CONNECTED'
    teg_patt = cTegPattern(r'\[EVT\]:')
    teg_patt.AddValuePattern(cValuePattern(r'BLE_GAP_EVT_CONNECTED', r'', r'', r''))
    parser.AddTegPattern(teg_patt)

##__clndr_check_md5: CLNDR MD5 compare OK
    teg_patt = cTegPattern(r'__clndr_check_md5:')
    teg_patt.AddValuePattern(cValuePattern(r'CLNDR MD5 compare OK',  r'' , r'', r''))
    parser.AddTegPattern(teg_patt)

##'__TB3_check_CZ_mode_and_set_auto: err Tion O2 RF connect'
##'__TB3_check_CZ_mode_and_set_auto: err Tion B3 connect'
##'__TB3_check_CZ_mode_and_set_auto: err Tion B4 connect'
    teg_patt = cTegPattern(r'__TB3_check_CZ_mode_and_set_auto:')
    teg_patt.AddValuePattern(cValuePattern(r'',  r':' , r'.+', r''))
    parser.AddTegPattern(teg_patt)

##'beacon_RX: 14124434, COORD_ID MAC: s, RSSI=32'
    teg_patt = cTegPattern(r'beacon_RX:')
    teg_patt.AddValuePattern(cValuePattern(RE_PATT_MULT_DIGITS,  r'', r'', r','))
    teg_patt.AddValuePattern(cValuePattern(r'COORD_ID MAC',  r':' , r' \w+', r','))
    teg_patt.AddValuePattern(cValuePattern(r'RSSI',  r'=' , RE_PATT_MULT_DIGITS, r''))
    parser.AddTegPattern(teg_patt)

## BleCentralManualConnectStart: start con for 84:DF:A4:25:B5:FC
    teg_patt = cTegPattern(r'BleCentralManualConnectStart:')
    teg_patt.AddValuePattern(cValuePattern(r' .+'+RE_PATT_MAC, r'' , r'', r''))
    parser.AddTegPattern(teg_patt)

##DevFileOp: st=idle, sID=0, dst=idleMAC-00:00:00:00:00:00, type=0, prg=0%
    teg_patt = cTegPattern(r'DevFileOp:')
    teg_patt.AddValuePattern(cValuePattern(r'st', r'=' , r'\w+', r','))
    teg_patt.AddValuePattern(cValuePattern(r'sID', r'=' , r'\d+', r','))
    teg_patt.AddValuePattern(cValuePattern(r'dst', r'=' , r'\w+-'+RE_PATT_MAC, r','))
    teg_patt.AddValuePattern(cValuePattern(r'type', r'=' , r'\d+', r','))
    teg_patt.AddValuePattern(cValuePattern(r'prg', r'=' , r'\d+%', r''))
    parser.AddTegPattern(teg_patt)

##recv frame: 0x2e02, ID=2530
    teg_patt = cTegPattern(r'recv frame:')
    teg_patt.AddValuePattern(cValuePattern(RE_PATT_HEX_DIGIT, r'' , r'', r','))
    teg_patt.AddValuePattern(cValuePattern(r'ID', r'=' , RE_PATT_MULT_DIGITS, r''))
    parser.AddTegPattern(teg_patt)

##RfCheckDevState: ERR CHECK DEV STATE FOR 0x1007, mac-BA:F7:10:4E:4A:68 errc=200
    teg_patt = cTegPattern(r'RfCheckDevState:')
    teg_patt.AddValuePattern(cValuePattern('ERR CHECK DEV STATE FOR '+RE_PATT_HEX_DIGIT, r'' , r'', r','))
    teg_patt.AddValuePattern(cValuePattern(r'mac', r'-' , RE_PATT_MAC, r''))
    teg_patt.AddValuePattern(cValuePattern(r'errc', r'=' , RE_PATT_MULT_DIGITS, r''))
    parser.AddTegPattern(teg_patt)

##wifi_scan_net: new try scan...
##wifi_scan_net: geneticunifi, rssi=-70, SecType=3, BSID-24:A4:3C:4D:0D:17
##wifi_scan_net: Keenetic-7363, rssi=-74, SecType=3, BSID-50:FF:20:0E:D8:76
##wifi_scan_net: DIRECT-56-HP M426 LaserJet, rssi=-75, SecType=3, BSID-9E:30:5B:8E:8B:56
##wifi_scan_net: duplicate entry
##wifi_scan_net: disable scan
    teg_patt = cTegPattern(r'wifi_scan_net:')
    teg_patt.AddValuePattern(cValuePattern('\w+ \w+ \w+\.\.\.', r'' , r'', r''))
    teg_patt.AddValuePattern(cValuePattern(r'd\w+ \w+', r'', r'', r'\b'))
    teg_patt.AddValuePattern(cValuePattern(r'[-\s\w]+', r'', r'', r', rssi'))
    teg_patt.AddValuePattern(cValuePattern(r'rssi', r'=', r'[-\d]+', r','))
    teg_patt.AddValuePattern(cValuePattern(r'SecType', r'=', RE_PATT_MULT_DIGITS, r','))
    teg_patt.AddValuePattern(cValuePattern(r'BSID', r'-', RE_PATT_MAC, r'\b'))
    parser.AddTegPattern(teg_patt)

##wifi_sync_cur_state: Sync OK, ID=0, pck_size=956, ping 209
    teg_patt = cTegPattern(r'wifi_sync_cur_state:')
    teg_patt.AddValuePattern(cValuePattern('[-\s\w]+', r'' , r'', r', ID'))
    teg_patt.AddValuePattern(cValuePattern(r'ID', r'=', RE_PATT_MULT_DIGITS, r','))
    teg_patt.AddValuePattern(cValuePattern(r'pck_size', r'=', RE_PATT_MULT_DIGITS, r','))
    teg_patt.AddValuePattern(cValuePattern(r'ping', r'\s', RE_PATT_MULT_DIGITS, r'\b'))
    parser.AddTegPattern(teg_patt)


    for text in text_list:
        print(parser.Parse(text))


if __name__ == '__main__':
    main()
