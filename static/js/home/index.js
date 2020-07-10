/*
    Theme Name: i-CityAssistant
    Author: Alcindo Schleder
    Author URL: https://icity.net.br
*/
const IndexEvents = function () {
    const showModalImage = function(href) {
        modalObj = $('#modalDetails');
        target = $('.modal-body').html('<img src="' + href + '" />');
        $('#modalimageData').html('Detalhes da Imagem');
        modalObj.modal('show');
    };
    const showModalAjax = function(href) {
        modalObj = $('#modalDetails');
        target = $('.modal-body');
        // get ajax data from url that is on href

        // show data
        modalObj.modal('show');
    };
    const DocumentsEvents = function () {
        let dt_table = $('.datatable').dataTable({
            language:  {
                url: "https://cdn.datatables.net/plug-ins/1.10.21/i18n/Portuguese-Brasil.json"
            }, // global variable defined in html
//            order: [[ 1, "fk_categories" ]],
            lengthMenu: [[25, 50, 100, 200], [25, 50, 100, 200]],
            columnDefs: [
                {
                    orderable: true,
                    searchable: true,
                    className: "center",
                    targets: [0, 1, 2, 3, 4, 5, 6, 7, 8]
                },
                {
                    data: 'thumbnail_image',
                    targets: [0],
                    render: function (data, type, full, meta) {
                        href = data.replace('thumbnail', 'high');
                        return '<a href="javascript:IndexEvents.showImage(\''  + href + '\')"><img class="img-fluid" src="' + data + '" style="height:50px;width:50px;"/></a>';
                    }
                },
                {
                    data: 'fk_categories',
                    targets: [1],
                    render: function (data, type, full, meta) {
                        href = '/category_detail/' + data;
                        return '<a href="javascript:showAjaxData(' + href + ')">' + data + '</a>';
                    }
                },
                {
                    data: 'pk_images',
                    targets: [2]
                },
                {
                    data: 'fk_user',
                    targets: [3]
                },
                {
                    data: 'image_size',
                    targets: [4]
                },
                {
                    data: 'image_width',
                    targets: [5]
                },
                {
                    data: 'image_height',
                    targets: [6]
                },
                {
                    data: 'image_type',
                    targets: [7]
                },
                {
                    data: 'flag_public',
                    targets: [8]
                }
            ],
            searching: true,
            processing: true,
            serverSide: true,
            stateSave: true,
            ajax: DT_PUBLIC_IMAGES
        });
    };
    const redirectPost = function(location, args) {
    };
    return {
        //main function to initiate the module
        Init: function () {
            DocumentsEvents();
        },
        showImage: function (href) {
            showModalImage(href)
        }
    };
}();

$(document).ready(function () {
    //normalize window.URL
    IndexEvents.Init()
});
