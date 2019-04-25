import newsletter

def main():
    app = newsletter.create_app()
    app.run(
        host="0.0.0.0",
        port=3012
    )

if __name__ == '__main__':
    main()