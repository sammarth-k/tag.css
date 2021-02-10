import getpass as gt

def top():
    topv = f"""
        <!DOCTYPE html>
    <html>
    <head>
        <title>{gt.getuser()}'s Tags</title>
        <meta name="author" content="Sammarth Kumar">
        <link href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.no-icons.min.css"
            rel="stylesheet">
        <link href="fa/css/all.css" rel="stylesheet">
        <link rel="shortcut icon" href="assets/favicon.ico" type="image/x-icon" />
        <link rel="apple-touch-icon" href="assets/apple-touch-icon.png" />
        <link rel="apple-touch-icon" sizes="57x57" href="assets/apple-touch-icon-57x57.png" />
        <link rel="apple-touch-icon" sizes="72x72" href="assets/apple-touch-icon-72x72.png" />
        <link rel="apple-touch-icon" sizes="76x76" href="assets/apple-touch-icon-76x76.png" />
        <link rel="apple-touch-icon" sizes="114x114" href="assets/apple-touch-icon-114x114.png" />
        <link rel="apple-touch-icon" sizes="120x120" href="assets/apple-touch-icon-120x120.png" />
        <link rel="apple-touch-icon" sizes="144x144" href="assets/apple-touch-icon-144x144.png" />
        <link rel="apple-touch-icon" sizes="152x152" href="assets/apple-touch-icon-152x152.png" />
        <link rel="apple-touch-icon" sizes="180x180" href="assets/apple-touch-icon-180x180.png" />
        <link rel="stylesheet" href="customtag.css">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div class="topnav" id="myTopnav">
            <a href="#home"><img style="padding-bottom:0.2rem;" width="38rem" height="auto" src="assets/logo.png"></a>
            <div id="links">
                <a onclick="toggle();"><i id="toggle" class="fas fa-sun" aria-hidden="true"></i></a>
                <a href="https://github.com/sammarth-k/tag.css"><i class="fab fa-github" aria-hidden="true"></i></a>
                <a href="#docs">Docs</a>
                <a href="#about">About</a>
            </div>
            <a href="javascript:void(0);" class="icon" onclick="myFunction()">&#9776;</a>
        </div>

        <div align="center"><br><br><br>
            <header>
                <img src="assets/banner.svg" width="250rem" height="auto"
                    class="img-fluid ${"3|rounded-top,rounded-right,rounded-bottom,rounded-left,rounded-circle,|"}" alt="">
            </header>
        </div>

        <div align="center" class="container">
            <h3>Responsive tags and flairs of different colors, shapes, fills and sizes</h3><br>
        <table class="table" align="center" style="text-align:center" id="linktable">
        """
    return topv

def table(color):
   row = """

        <td>
            <a href="#{}">{}</a>
        </td>
   """.format(color.lower(),color)
   return row

def showcase(color, normal, hollow):
    show = """
    <h3 id="{}">{}</h3>
        <div class="row">
            
            <div class="col-sm">
                <tag class="tag-small {}">Sample Text</tag><br><br>
                <tag class="{}">Sample Text</tag><br><br>
                <tag class="tag-large {}">Sample Text</tag><br><br>
                <tag class="tag-xl {}">Sample Text</tag><br><br>
                <p>Solid</p>

            </div>
            <div class="col-sm">
                <tag class="tag-small {}">Sample Text</tag><br><br>
                <tag class="{}">Sample Text</tag><br><br>
                <tag class="tag-large {}">Sample Text</tag><br><br>
                <tag class="tag-xl {}">Sample Text</tag><br><br>
                
                <p>Hollow</p>
            </div>
            <div class="col-sm">
                <tag class="tag-small tag-rounded {}">Sample Text</tag><br><br>
                <tag class="tag-rounded {}">Sample Text</tag><br><br>
                <tag class="tag-large tag-rounded {}">Sample Text</tag><br><br>
                <tag class="tag-xl tag-rounded {}">Sample Text</tag><br><br>
                <p>Rounded Solid</p>
            </div>
            <div class="col-sm">
                <tag class="tag-small tag-rounded {}">Sample Text</tag><br><br>
                <tag class="tag-rounded {}">Sample Text</tag><br><br>
                <tag class="tag-large tag-rounded {}">Sample Text</tag><br><br>
                <tag class="tag-xl tag-rounded {}">Sample Text</tag><br><br>

                <p>Rounded Hollow</p>
            </div>
        </div>
        <br>
        
        """.format(color.lower(), color, normal, normal, normal, normal, hollow, hollow, hollow, hollow, normal, normal, normal, normal, hollow, hollow, hollow, hollow)
    return show


def bottom():
    bottomv = """
      </div>
        </body>
        <script src="script.js">
        </script>

        </html>

    """
    return bottomv
