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
    const showModalAjax = function(href, title) {
        const promise = new Promise((resolve, reject) => {
            modalObj = $('#modalDetails');
            target = $('.modal-body');
            $('#modalTitle').html('Detalhes da ' + title);
            $.ajax({
                type: "GET",
                url: href,
                success: function(data) {
                    target.html(data);
                    modalObj.modal('show')
                    resolve(true)
                },
                error: function(jqXHR, textStatus, errorThrown) {
                    let msg = 'Um erro ocorreu ao chamar a API: status(' + textStatus + ') erro( ' + errorThrown + ')';
                    target.html(msg)
                    console.log('erro....', msg);
                    reject(false)
                },
                dataType: "text"
            });
        })
        return promise;
    };
    const saveFormData = function(form) {
        modalObj = $('#modalDetails');
        target = $('.modal-body');
        data = form.serialize();
        // get ajax data from url that is on href
        $.ajax({
            type: form.attr('method'),
            url: form.attr('action'),
            data: data,
            success: function(data) {
                target.html(data);
                console.log('success: ', data);
                modalObj.modal('hide');
            },
            error: function(jqXHR, textStatus, errorThrown) {
                let msg = 'Um erro ocorreu ao chamar a API: status(' + textStatus + ') erro( ' + errorThrown + ')';
                target.html(msg)
                console.log('erro....', msg);
            },
            dataType: "json"
        });
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
                        let pk = data.substring(0, data.indexOf(' - '));
                        href = '/category_detail/' + pk;
                        return '<a href="javascript:IndexEvents.showAjaxData(\'' + href + '\', 0)">' + data + '</a>';
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
        },
        showAjaxData: function (href, modalType, op='opInsert') {
            let opDsc = 'Criar';
            if (op == 'opUpdate') {
                opDsc = 'Editar';
            };
            if (op == 'opDelete') {
                opDsc = 'Excluir';
            };
            let title = 'Categoria';
            if (modalType == 1) {
                title = 'Imagem';
            };
            title = opDsc + ' ' + title;
            showModalAjax(href, title).then(res => {
                return $('#form-modal').on('submit', (e) => {
                    e.preventDefault();
                    console.log("form submitted!");  // sanity check
                    if (modalType == 0)
                        saveFormData($('#form-modal'));
                    if (modalType == 1)
                        saveImage($('#form-modal'));
                });
            });
        }
    };
}();

$(document).ready(function () {
    //normalize window.URL
    IndexEvents.Init()
});
