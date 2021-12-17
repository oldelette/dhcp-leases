import sys
from pyparsing import Word, alphas, Suppress, Combine, nums, string, Optional, Regex
from time import strftime
from dataclasses import dataclass


@dataclass
class LogItem:
    timestamp: str
    hostname: str
    appname: str
    pidnum: str
    message: str


@dataclass
class Parser(object):
    def get_rule(self):
        ints = Word(nums)
        month = Word(string.ascii_uppercase, string.ascii_lowercase, exact=3)
        day = ints
        hour = Combine(ints + ":" + ints + ":" + ints)
        rule1 = month + day + hour  # timestamp
        rule2 = Word(alphas + nums + "_" + "-" + ".")  # hostname
        rule3 = Word(alphas + "/" + "-" + "_" + ".")  # appname
        rule4 = Combine("[" + ints + "." + ints + "]")  # pidnum
        rule5 = Regex(".*")  # message

        return rule1 + rule2 + rule3 + rule4 + rule5

    def parse(self, line):
        rule = self.get_rule()
        parsed = rule.parseString(line)

        return vars(
            LogItem(
                timestamp=strftime("%Y-%m-%d %H:%M:%S"),
                hostname=parsed[3],
                appname=parsed[4],
                pidnum=parsed[5],
                message=parsed[6],
            )
        )


""" --------------------------------- """


def main():
    parser = Parser()

    if len(sys.argv) == 1:
        print("Usage:\n  $ python xlog.py ./sample.log")
        exit(666)

    syslogPath = sys.argv[1]

    with open(syslogPath) as syslogFile:
        for line in syslogFile:
            print("--" * 20)
            print(line)
            fields = parser.parse(line)
            print(fields)


if __name__ == "__main__":
    main()
