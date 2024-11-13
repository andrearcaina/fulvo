$(document).ready(function() {
    $('#allUS').click(function() {
        getTableData("user");
    });
    $('#allPS').click(function() {
        getTableData("player");
    });
    $('#allRS').click(function() {
        getTableData("referee");
    });
    $('#allTS').click(function() {
        getTableData("team");
    });
    $('#allHL').click(function() {
        getTableData("house-league");
    });
    $('#allMS').click(function() {
        getTableData("match-stats");
    });
    $('#allMR').click(function() {
        getTableData("match-referees");
    });

    function getTableData(table) {
        const ENDPOINT = "/api/" + table + "/read";
        $.ajax({
            url: ENDPOINT,
            type: "GET",
            success: function(resp) {
                console.log(resp);
                renderTable(resp);
            },
            error: (error) => console.log(error)
        });
    }

    function renderTable(data) {
        let table = $("<table class='table table-bordered table-hover'></table>");
        let thead = $("<thead></thead>");
        let tbody = $("<tbody></tbody>");
        var tr = $("<tr></tr>");

        for (let key in data[0]) {
            tr.append("<th>" + key + "</th>");
        }

        thead.append(tr);
        table.append(thead);

        for (let i = 0; i < data.length; i++) {
            let tr = $("<tr></tr>");
            for (let key in data[i]) {
                tr.append("<td>" + data[i][key] + "</td>");
            }
            tbody.append(tr);
        }

        table.append(tbody);
        $("#buttonOutput").html(table);    
    }
});