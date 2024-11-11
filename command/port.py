
def cmd_port(args):
    if args.ps:
        pass

    if args.allocate:
        pass

    if args.query:
        pass

    if args.delete:
        pass

    print(**args)

# curl -X 'GET' \
#   'http://stag.localhost:8000/port/allocate/xhl' \
#   -H 'accept: application/json'

# curl -X 'GET' \
#   'http://stag.localhost:8000/port/query/xhl' \
#   -H 'accept: application/json'

# curl -X 'DELETE' \
#   'http://stag.localhost:8000/port/del/xhl1' \
#   -H 'accept: application/json'
