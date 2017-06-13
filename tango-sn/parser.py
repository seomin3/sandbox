import re

class parser(object):
    filename = ''
    parser_type = ''
    data = []
    parsed_data = []

    def __init__(self, csv, parser_type):
        self.filename = csv
        self.parser_type = parser_type

    def append_data(self):
        try:
            if self.parser_type == 'server' and self.data[2] == 'VM':
                self.parsed_data.append([self.data[1],  # tenant
                                         re.sub(r'[\xc2\xa0]', '', self.data[3]),  # name
                                         self.data[8],   # network
                                         self.data[7],   # 90 net
                                         self.data[9],   # 60 net
                                         self.data[11],  # 150 net
                                         self.data[13],  # 70 net
                                         self.data[15]])   # 220 net
            elif self.parser_type == 'epg':
                if not self.data[1].isalpha(): return False
                self.parsed_data.append([self.data[1],  # subnet
                                         self.data[0],  # name
                                         re.sub(r'\r\n', '', self.data[2])]) # dhcp
        except IndexError:
            #print('unexcept error: %s' % self.data)
            return False

    def read(self):
        self.parsed_data = []
        with open(self.filename) as excel_data:
            while True:
                self.data = excel_data.readline()
                if not self.data: break
                self.data = self.data.split(",")
                self.append_data()
        return self.parsed_data

if __name__ == "__main__":
    main()