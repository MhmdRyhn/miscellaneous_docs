# Your input PATH have to be valid. 
# Otherwise you will get a 0(ZERO) as your OUTPUT.



import os


class NoOFLinesInAProject:
    project_path = ''

    def __init__(self):
        self.project_path = input('Enter Project Path: ')

    def total_lines(self):
        filecnt, readablefilecnt, cnt = 0, 0, 0

        for dirpath, dirnames, filenames in os.walk(self.project_path):
            for names in filenames:
                filecnt += 1
                f_path = os.path.join(dirpath, names)
                f_state = open(f_path, 'r')

                f_lines = None
                try:
                    f_lines = f_state.readlines()
                    readablefilecnt += 1
                    cnt += len(f_lines)
                except:
                    if UnicodeDecodeError:
                        pass

        return [filecnt, readablefilecnt, cnt]


if __name__ == '__main__':
    linecnt = NoOFLinesInAProject()
    total = linecnt.total_lines()
    print('Total files: ', total[0])
    print('Readable files: ', total[1])
    print('Total lines: ', total[2])
