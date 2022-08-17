from argparse import ArgumentParser
import slackweb
import toml

parser = ArgumentParser()
parser.add_argument('text', nargs='+')
parser.add_argument('--secret', default='./secret.toml')
args = parser.parse_args()

secret = toml.load(args.secret)

slack = slackweb.Slack(
    url=secret['secret']['url'])
mes = ''
for t in args.text:
    mes += str(t) + '\n'

slack.notify(text=mes)
