// this function makes a GET request to the server to get all the data from a specific table
export function getTableData(table) {
    const ENDPOINT = "/api/" + table + "/read";
    $.ajax({
        url: ENDPOINT,
        type: "GET",
        success: function(resp) {
            renderModelTable(table, resp, "allOutput");
        },
        error: function(error) {
            console.error(error);
            $("#buttonOutput").html("No record found");
        }
    });
}

// this function makes a GET request to the server
// to get data from a specific table and a specific ID from that table
export function getTableDataByID(table, id) {
    const ENDPOINT = "/api/" + table + "/read/" + id;
    $.ajax({
        url: ENDPOINT,
        type: "GET",
        success: function(resp) {
            renderModelTable(table, resp, "searchOutput");
        },
        error: function(error) {
            console.error(error);
            $("#searchOutput").html("No record found");
        }
    });
}

// makes a POST request and creates a record in the table based on user input
export function createRecord(table, data) {
    const ENDPOINT = "/api/" + table + "/create";
    $.ajax({
        url: ENDPOINT,
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function(resp) {
            $("#createOutput").html("Record created successfully");
        },
        error: function(error) {
            console.error(error);
            $("#createOutput").html("Error creating record");
        }
    });
}

// makes a PUT request and updates the current cell's data
function updateCellData(table, id, data) {
    const ENDPOINT = "/api/" + table + "/update/" + id;
    $.ajax({
        url: ENDPOINT,
        type: "PUT",
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function(resp) {
            $("#changeRowOutput").html("Cell updated successfully");
        },
        error: function(error) {
            console.error(error);
            $("#changeRowOutput").html("Error updating cell. Please try again.");
        }
    });
}

// make a DELETE request and deletes the row from the database
export function deleteRecord(table, id, id2, row) {
    let ENDPOINT;

    if (parseInt(id2) && id2.length >= 1 && !id2.includes("-")) {
        ENDPOINT = "/api/" + table + "/delete/" + id + "/" + id2;
    } else {
        ENDPOINT = "/api/" + table + "/delete/" + id;
    }

    console.log(ENDPOINT);
    
    $.ajax({
        url: ENDPOINT,
        type: "DELETE",
        success: function(resp) {
            console.log(resp);
            row.remove();
        },
        error: function(error) {
            console.error(error);
            $("#changeRowOutput").html("Error deleting record");
        }
    });
}

// updates Database dependent on action the user takes
export function updateDatabase(action) {
    const ENDPOINT = "/api/menu/" + action;
    $.ajax({
        url: ENDPOINT,
        type: action === "queries" ? "GET" : "POST",
        success: function(resp) {
            console.log(resp);
            if (action !== "queries") {
                $("#resultDB").html(resp.message);
            } else {
                renderQueries(resp.results, "resultDB");
            }
        },
        error: function(error) {
            console.error(error);
            $("#resultDB").html("Error in executing script in database");
        }
    });
}

// this function renders the data in a table format
function renderModelTable(specificTable, data, htmlID) {        
    let [table, thead, tbody, trHead, trBody] = initTable();

    if (data.length > 0) {
        for (let key in data[0]) {
            trHead.append("<th>" + key + "</th>");
        }
        trHead.append("<th>Delete</th>");
        thead.append(trHead);
        table.append(thead);

        for (let i = 0; i < data.length; i++) {
            let tr = $("<tr></tr>");
            
            for (let key in data[i]) {
                let td = $("<td contenteditable='true'></td>").text(data[i][key]);
                tr.append(cellFunctionality(td, key, specificTable));
                appendDeleteButton(tr, key, data[i], specificTable);
            }
            tbody.append(tr);
        }
    } else {
        for (let key in data) {
            trHead.append("<th>" + key + "</th>");
        }
        thead.append(trHead);
        table.append(thead);

        for (let key in data) {
            trBody.append("<td>" + data[key] + "</td>");   
        }
        tbody.append(trBody);
    }

    table.append(tbody);
    $("#"+htmlID).html(table);    
}

// updates additional fields in users.html file dependent on user input
export function updateRoleFields() { 
    let role = $("#createRole").val();
    if (role === "player") {
        $("#playerFields").show();
        $("#refereeFields").hide();
    } else if (role === "referee") {
        $("#playerFields").hide();
        $("#refereeFields").show();
    } else {
        $("#playerFields").hide();
        $("#refereeFields").hide();
    }
}

// this function specifically only renders table data from the queries button in home page
function renderQueries(data, htmlID) {
    $("#" + htmlID).empty();

    for (let i = 0; i < data.length; i++) {
        let [table, thead, tbody, trHead, _] = initTable();

        // Create table headers
        for (let key in data[i][0]) {
            trHead.append("<th>" + key + "</th>");
        }
        thead.append(trHead);
        table.append(thead);

        // Create table body
        for (let j = 0; j < data[i].length; j++) {
            let trBody = $("<tr></tr>");
            for (let key in data[i][j]) {
                trBody.append("<td>" + data[i][j][key] + "</td>");
            }
            tbody.append(trBody);
        }
        table.append(tbody);
        $("#" + htmlID).append(table);
    }
}

function initTable() {
    let table = $("<table class='table table-bordered table-hover'></table>");
    let thead = $("<thead></thead>");
    let tbody = $("<tbody></tbody>");
    let trHead = $("<tr></tr>");
    let trBody = $("<tr></tr>");

    return [table, thead, tbody, trHead, trBody];
}

// adds the functionality to the current cell (allows for changing the cell data)
function cellFunctionality(td, key, specificTable) {
    td.on("focus", function() {
        $(this).data("originalValue", $(this).text());
    });
    td.on("blur", function() {
        let newValue = $(this).text();
        let originalValue = $(this).data("originalValue");
        
        if (newValue !== originalValue) {
            let userId = $(this).closest("tr").find("td:first").text();
            let updateData = {};
        
            updateData[key] = newValue;
            updateCellData(specificTable, userId, updateData);
        }
    });

    return td;
}

// appends the delete button to the last cell in the row
function appendDeleteButton(tr, key, data, specificTable) {
    if (key === Object.keys(data)[Object.keys(data).length - 1]) {
        let deleteBtn = $("<button class='btn btn-danger'>Delete</button>");
        deleteBtn.on("click", function() {
            let userId = $(this).closest("tr").find("td:first").text();
            let secondID = $(this).closest("tr").find("td:nth-child(2)").text();

            deleteRecord(specificTable, userId, secondID, $(this).closest("tr"));
        });
        
        let tdDelete = $("<td></td>").append(deleteBtn);
        tr.append(tdDelete);
    }
}