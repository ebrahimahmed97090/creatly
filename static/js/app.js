/*slider*/
$(document).ready(function () {
    $("#testimonial-slider").owlCarousel({
        items: 3,
        itemsDesktop: [15, 3],
        itemsDesktopSmall: [15, 2],
        itemsTablet: [15, 2],
        itemsMobile: [15, 1],
        pagination: true,
        autoPlay: true
    });
});

$('.dragitms>div').draggable({
    appendTo: 'body',
    helper: 'clone',
    addClass: true,
    cursor: "crosshair",
    refreshPositions: true,
    scope: "builder",
    scroll: false
});

$('.cnt').droppable({
    scope: "builder",
    drop: (event, ui) => {
        console.log($(ui)[0].draggable)
        if ($(ui)[0].draggable.hasClass('covers')) {

            $(".cnt").append('\n' +
                '    <div class="site-wrapper">\n' +
                '\n' +
                '      <div class="site-wrapper-inner">\n' +
                '\n' +
                '        <div class="container">\n' +
                '\n' +
                '          <div class="masthead clearfix">\n' +
                '            <div class="container inner">\n' +
                '              <h3 class="masthead-brand">Cover</h3>\n' +
                '              <nav>\n' +
                '                <ul class="nav masthead-nav">\n' +
                '                  <li class="active"><a href="#">Home</a></li>\n' +
                '                  <li><a href="#">Features</a></li>\n' +
                '                  <li><a href="#">Contact</a></li>\n' +
                '                </ul>\n' +
                '              </nav>\n' +
                '            </div>\n' +
                '          </div>\n' +
                '\n' +
                '          <div class="inner cover">\n' +
                '            <h1 class="cover-heading">Cover your page.</h1>\n' +
                '            <p class="lead">Cover is a one-page template for building simple and beautiful home pages. Download, edit the text, and add your own fullscreen background photo to make it your own.</p>\n' +
                '            <p class="lead">\n' +
                '              <a href="#" class="btn btn-lg btn-default">Learn more</a>\n' +
                '            </p>\n' +
                '          </div>\n' +
                '\n' +
                '        </div>\n' +
                '\n' +
                '      </div>\n' +
                '\n' +
                '    </div>')
        } else if ($(ui)[0].draggable.hasClass('banner')) {
            $(".cnt").append('<div class="alert alert-primary" role="alert">A simple primary alert—check it out! </div>')

        } else if ($(ui)[0].draggable.hasClass('slider')) {
            $(".cnt").append('<div id="carouselExampleCaptions" class="carousel slide" data-ride="carousel"><ol class="carousel-indicators"><li data-target="#carouselExampleCaptions" data-slide-to="0" class="active"></li><li data-target="#carouselExampleCaptions" data-slide-to="1"></li><li data-target="#carouselExampleCaptions" data-slide-to="2"></li></ol><div class="carousel-inner"><div class="carousel-item active"><img src="..." class="d-block w-100" alt="..."><div class="carousel-caption d-none d-md-block"><h5>First slide label</h5><p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p></div></div><div class="carousel-item"><img src="..." class="d-block w-100" alt="..."><div class="carousel-caption d-none d-md-block"><h5>Second slide label</h5><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p></div></div><div class="carousel-item"><img src="..." class="d-block w-100" alt="..."><div class="carousel-caption d-none d-md-block"><h5>Third slide label</h5><p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p></div></div></div><a class="carousel-control-prev" href="#carouselExampleCaptions" role="button" data-slide="prev"><span class="carousel-control-prev-icon" aria-hidden="true"></span> <span class="sr-only">Previous</span></a> <a class="carousel-control-next" href="#carouselExampleCaptions" role="button" data-slide="next"><span class="carousel-control-next-icon" aria-hidden="true"></span> <span class="sr-only">Next</span></a></div>')

        } else if ($(ui)[0].draggable.hasClass('text-block')) {
            $(".cnt").append('<blockquote class="blockquote text-right"><p class="mb-0">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p><footer class="blockquote-footer">Someone famous in <cite title="Source Title">Source Title</cite></footer></blockquote>')

        } else if ($(ui)[0].draggable.hasClass('titles')) {
            $(".cnt").append('<h1>Click to Edit the heading</h1>')

        } else if ($(ui)[0].draggable.hasClass('pic')) {
            $(".cnt").append('<img src="..." class="img-fluid" alt="Responsive image">')

        } else if ($(ui)[0].draggable.hasClass('features')) {
            $(".cnt").append('<div class="container"><div class="row"><div class="col-12 col-sm-8 col-md-6 col-lg-4"><div class="card"><img class="card-img-top" src="https://s3.eu-central-1.amazonaws.com/bootstrapbaymisc/blog/24_days_bootstrap/oslo.jpg" alt="Bologna"><div class="card-body text-center"><img class="avatar rounded-circle" src="https://s3.eu-central-1.amazonaws.com/bootstrapbaymisc/blog/24_days_bootstrap/robert.jpg" alt="Bologna"><h4 class="card-title">Robert Downey Jr.</h4><h6 class="card-subtitle mb-2 text-muted">Famous Actor</h6><p class="card-text">Robert John Downey Jr.\'career has included critical and popular success in his youth, followed by a period of substance abuse and legal difficulties, and a resurgence of commercial success in middle age.</p><a href="#" class="btn btn-info">Follow</a> <a href="#" class="btn btn-outline-info">Message</a></div></div></div><div class="col-12 col-sm-8 col-md-6 col-lg-4"><div class="card"><img class="card-img-top" src="https://s3.eu-central-1.amazonaws.com/bootstrapbaymisc/blog/24_days_bootstrap/oslo.jpg" alt="Bologna"><div class="card-body text-center"><img class="avatar rounded-circle" src="https://s3.eu-central-1.amazonaws.com/bootstrapbaymisc/blog/24_days_bootstrap/robert.jpg" alt="Bologna"><h4 class="card-title">Robert Downey Jr.</h4><h6 class="card-subtitle mb-2 text-muted">Famous Actor</h6><p class="card-text">Robert John Downey Jr.\'career has included critical and popular success in his youth, followed by a period of substance abuse and legal difficulties, and a resurgence of commercial success in middle age.</p><a href="#" class="btn btn-info">Follow</a> <a href="#" class="btn btn-outline-info">Message</a></div></div></div><div class="col-12 col-sm-8 col-md-6 col-lg-4"><div class="card"><img class="card-img-top" src="https://s3.eu-central-1.amazonaws.com/bootstrapbaymisc/blog/24_days_bootstrap/oslo.jpg" alt="Bologna"><div class="card-body text-center"><img class="avatar rounded-circle" src="https://s3.eu-central-1.amazonaws.com/bootstrapbaymisc/blog/24_days_bootstrap/robert.jpg" alt="Bologna"><h4 class="card-title">Robert Downey Jr.</h4><h6 class="card-subtitle mb-2 text-muted">Famous Actor</h6><p class="card-text">Robert John Downey Jr.\'career has included critical and popular success in his youth, followed by a period of substance abuse and legal difficulties, and a resurgence of commercial success in middle age.</p><a href="#" class="btn btn-info">Follow</a> <a href="#" class="btn btn-outline-info">Message</a></div></div></div></div></div>')

        } else if ($(ui)[0].draggable.hasClass('cols')) {
            $(".cnt").append('<div class="row"><div class="col"><div class="card" style="width:18rem"><img src="..." class="card-img-top" alt="..."><div class="card-body"><h5 class="card-title">Card title</h5><p class="card-text">Some quick example text to build on the card title and make up the bulk of the card\'s content.</p><a href="#" class="btn btn-primary">Go somewhere</a></div></div></div><div class="col"><div class="card" style="width:18rem"><img src="..." class="card-img-top" alt="..."><div class="card-body"><h5 class="card-title">Card title</h5><p class="card-text">Some quick example text to build on the card title and make up the bulk of the card\'s content.</p><a href="#" class="btn btn-primary">Go somewhere</a></div></div></div><div class="col"><div class="card" style="width:18rem"><img src="..." class="card-img-top" alt="..."><div class="card-body"><h5 class="card-title">Card title</h5><p class="card-text">Some quick example text to build on the card title and make up the bulk of the card\'s content.</p><a href="#" class="btn btn-primary">Go somewhere</a></div></div></div></div>')

        } else if ($(ui)[0].draggable.hasClass('nuamberssy')) {
            $(".cnt").append('<ul class="chart"><li class="axis"><div class="label">MVP</div><div class="label">All Star</div><div class="label">Slugger</div><div class="label">Rookie</div><div class="label">Triple A</div></li><li class="bar teal" style="height:95%" title="95"><div class="percent">95<span>%</span></div><div class="skill">Karate</div></li><li class="bar salmon" style="height:90%" title="90"><div class="percent">90<span>%</span></div><div class="skill">Taekwondo</div></li><li class="bar peach" style="height:80%" title="80"><div class="percent">80<span>%</span></div><div class="skill">Nunchucks</div></li><li class="bar lime" style="height:75%" title="75"><div class="percent">75<span>%</span></div><div class="skill">Bow Staff</div></li><li class="bar grape" style="height:40%" title="40"><div class="percent">40<span>%</span></div><div class="skill">Suplex</div></li></ul>')

        } else if ($(ui)[0].draggable.hasClass('text-image')) {
            $(".cnt").append('<div class="row"><div class="col"><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi blanditiis deserunt distinctio dolorem quibusdam quo saepe unde? Asperiores cumque ipsum magnam provident repellat. Architecto, consectetur non quibusdam soluta tempore voluptatum.</p></div><div class="col"><img src="" alt=""></div></div>')

        } else if ($(ui)[0].draggable.hasClass('image-text')) {
            $(".cnt").append('<div class="row"><div class="col"><img src="" alt=""></div><div class="col"><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi blanditiis deserunt distinctio dolorem quibusdam quo saepe unde? Asperiores cumque ipsum magnam provident repellat. Architecto, consectetur non quibusdam soluta tempore voluptatum.</p></div></div>')

        } else if ($(ui)[0].draggable.hasClass('pageheader')) {
            $(".cnt").append('<ul class="nav nav-tabs"><li class="nav-item"><a class="nav-link active" href="#">Active</a></li><li class="nav-item dropdown"><a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">Dropdown</a><div class="dropdown-menu"><a class="dropdown-item" href="#">Action</a> <a class="dropdown-item" href="#">Another action</a> <a class="dropdown-item" href="#">Something else here</a><div class="dropdown-divider"></div><a class="dropdown-item" href="#">Separated link</a></div></li><li class="nav-item"><a class="nav-link" href="#">Link</a></li><li class="nav-item"><a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a></li></ul>')

        } else if ($(ui)[0].draggable.hasClass('imagesrow')) {
            $(".cnt").append('<div class="container-fluid"><div class="d-flex flex-row flex-wrap justify-content-center"><div class="d-flex flex-column"><img src="https://images.unsplash.com/photo-1485963631004-f2f00b1d6606?auto=format&fit=crop&w=668&q=80" class="img-fluid"> <img src="https://images.unsplash.com/photo-1502865787650-3f8318917153?auto=format&fit=crop&w=334&q=80" class="img-fluid"></div><div class="d-flex flex-column"><img src="https://images.unsplash.com/photo-1500816558239-6b91f4256ead?auto=format&fit=crop&w=331&q=80" class="img-fluid"> <img src="https://images.unsplash.com/photo-1487376318617-f43c7b41e2e2?auto=format&fit=crop&w=750&q=80" class="img-fluid scale"></div><div class="d-flex flex-column"><img src="https://images.unsplash.com/photo-1497888329096-51c27beff665?auto=format&fit=crop&w=751&q=80" class="img-fluid scale mb-2"> <img src="https://images.unsplash.com/photo-1505253468034-514d2507d914?auto=format&fit=crop&w=334&q=80" class="img-fluid"></div><div class="d-flex flex-column"><img src="https://images.unsplash.com/photo-1502550900787-e956c314a221?auto=format&fit=crop&w=334&q=80" class="img-fluid m-1 p-1"> <img src="https://images.unsplash.com/photo-1455853659719-4b521eebc76d?auto=format&fit=crop&w=750&q=80" class="img-fluid image m-1 p-1"></div></div></div>')

        } else if ($(ui)[0].draggable.hasClass('nuamberssy')) {
            $(".cnt").append('')

        } else if ($(ui)[0].draggable.hasClass('nuamberssy')) {
            $(".cnt").append('')

        }
        $(".cnt").find("*").attr('contenteditable', true);

    }
})
;
