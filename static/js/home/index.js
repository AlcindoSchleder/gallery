/*
    Theme Name: i-CityAssistant
    Author: Alcindo Schleder
    Author URL: https://icity.net.br
*/
const IndexEvents = function () {
    const DocumentsEvents = function () {
        const TESTMODEL_LIST_JSON_URL = '{% url "list_public_images" %}';
        // translations for datatables

        const dt_language = {
            "pk_images":      "{% 'Código' %}",
            "emptyTable":     "{% trans 'No data available in table' %}",
            "info":           "{% trans 'Showing _START_ to _END_ of _TOTAL_ entries' %}",
            "infoEmpty":      "{% trans 'Showing 0 to 0 of 0 entries' %}",
            "infoFiltered":   "{% trans '(filtered from _MAX_ total entries)' %}",
            "infoPostFix":    "",
            "thousands":      ",",
            "lengthMenu":     "{% trans 'Show _MENU_ entries' %}",
            "loadingRecords": "{% trans 'Loading...' %}",
            "processing":     "{% trans 'Processing...' %}",
            "search":         "{% trans 'Search:' %}",
            "zeroRecords":    "{% trans 'No matching records found' %}",
            "paginate": {
                "first":      "{% trans 'First' %}",
                "last":       "{% trans 'Last' %}",
                "next":       "{% trans 'Next' %}",
                "previous":   "{% trans 'Previous' %}"
            },
            "aria": {
                "sortAscending":  "{% trans ': activate to sort column ascending' %}",
                "sortDescending": "{% trans ': activate to sort column descending' %}"
            }
        }
        let dt_table = $('.datatable').dataTable({
            language: dt_language,  // global variable defined in html
            order: [[ 0, "desc" ]],
            lengthMenu: [[25, 50, 100, 200], [25, 50, 100, 200]],
            columnDefs: [
                {orderable: true,
                 searchable: true,
                 className: "center",
                 targets: [0, 1]
                },
                {
                    data: 'name',
                    targets: [0]
                },
                {
                    data: 'description',
                    targets: [1]
                }
            ],
            searching: true,
            processing: true,
            serverSide: true,
            stateSave: true,
            ajax: TESTMODEL_LIST_JSON_URL
        });
    };
    const redirectPost = function(location, args) {
    }
    return {
        //main function to initiate the module
        Init: function () {
            DocumentsEvents();
        }
    };
}();

$(document).ready(function () {
    //normalize window.URL
    IndexEvents.Init()
});
