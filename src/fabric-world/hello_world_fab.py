import fabric


def main():
    # machines = ['192.168.1.6']
    con = fabric.Connection('192.168.1.6',user='raj', connect_kwargs={"password": "aaaaaaaa"})
    con.run('ls -l')


if __name__ == "__main__":
    main()

