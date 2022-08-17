from argparse import ArgumentParser
import slackweb

parser = ArgumentParser()
parser.add_argument('text', nargs='+')
args = parser.parse_args()

url='put your webhook url into here'

slack = slackweb.Slack(
    url=url)
mes = ''
for t in args.text:
    mes += str(t) + '\n'

slack.notify(text=mes)
