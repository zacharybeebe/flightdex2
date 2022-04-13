function onAddResourceInitLabel(){
    var l = document.createElement('label');
    l.className = 'nav-link text-info';
    l.onclick = function(){onAddResource(this)};
    l.innerHTML = feather.icons['plus'].toSvg().trim();
    l.appendChild(document.createTextNode('Add Resource'));
    return l;
};


function onAddResourceNewLabel(elem){
    var l = document.createElement('label');
    l.className = 'nav-link text-info';
    l.style.cursor = 'pointer'
    l.dataset.value = elem.value;
    l.dataset.uuid = elem.dataset.uuid;
    l.dataset.url = `${window.origin}/resource_${elem.value}`
    l.addEventListener('click', function(event){onAddResourceLabelClickEvent(event, this)});
    l.innerHTML = feather.icons['edit'].toSvg().trim();
    l.appendChild(document.createTextNode(elem.value));
    return l;
};


function onAddResourceNewInput(placeholder, editing, uuid){
    var i = document.createElement('input');
    i.type = 'text';
    i.className = 'nav-link form-control';
    i.placeholder = placeholder;
    i.dataset.editing = editing;
    if (uuid === null){
        i.dataset.uuid = uuidv4();
    } else {
        i.dataset.uuid = uuid;
    }
    i.addEventListener('keyup', function(event){
        if (event.keyCode === 13) {
            if (this.value != ''){
                this.blur()
            }
        }
    });
    i.addEventListener('focusout', function(event){
        onAddResourceInputFocusOut(this)
    });
    return i
};


function onAddResourceNewLi(){
    var li = document.createElement('li');
    li.className = 'nav-item';

    var l = onAddResourceInitLabel();
    li.appendChild(l);
    return li;
};


function onAddResourceLabelClickEvent(event, elem){
    if (event.target.nodeName == 'LABEL'){
        var current_loc = window.location.pathname.split('_');
        if (current_loc.length > 1){
            if (current_loc[0] == '/resource'){
                var returns = gatherDivPdl(decodeURI(current_loc[1]));
                if (returns === false){
                    alert('Errors or required data needed to be corrected or filled, cannot advance')
                    return;
                }
                var [find_by, elements] = returns;
                console.log(find_by)
                console.log(elements)
                if (Object.keys(elements).length == 0) {
                    window.location = elem.dataset.url;
                    return;
                }
                fetch(`${window.origin}/submit_edits_${find_by}`, {
                    method: 'POST',
                    credentials: 'include',
                    body: JSON.stringify(elements), //JSON.stringify([find_by, elements]),
                    cache: 'no-cache',
                    headers: new Headers({
                        'content-type': 'application/json'
                    })
                })
                .then(function(response) {
                    if (response.status !== 200) {
                        console.log(`Response was not 200: ${response.status}`);
                    } else {
                        window.location = elem.dataset.url;
                    }
                })
            } else {
                window.location = elem.dataset.url;
            }
        } else {
            window.location = elem.dataset.url;
        }
    } else {
        onAddResource(elem, placeholder=elem.dataset.value, editing=true, uuid=elem.dataset.uuid, url=elem.dataset.url);
    }
};


function onAddResourceInputFocusOut(elem){
    console.log(elem.value)
    if (elem.value != ''){
        // Fetch HERE
        obj = {
            uuid: elem.dataset.uuid,
            label: elem.value,
            editing: elem.dataset.editing
        };
        fetch(`${window.origin}/resource_init_fetch`, {
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(obj),
            cache: 'no-cache',
            headers: new Headers({
                'content-type': 'application/json'
            })
        })
        .then(function(response) {
            if (response.status !== 200) {
                console.log(`Response was not 200: ${response.status}`);
            } else {
                response.json().then(function(data){
                    var res = data[0];
                    if (res.message == 'error'){
                        elem.style.color = 'red';
                        elem.focus()
                        return;
                    } else {
                        if (res.message == 'resource added to db' || res.message == 'resource updated in db'){
                            elem.value = res.new_label;
                        }
                        var l = onAddResourceNewLabel(elem);
                        elem.replaceWith(l);

                        if (elem.dataset.editing == 'false') {
                            var ul = document.getElementById('resource_list');
                            ul.appendChild(onAddResourceNewLi());
                        }
                        return;
                    }
                })
            }
        })
    } else {
        if (elem.dataset.editing == 'false'){
            var l = onAddResourceInitLabel();
            elem.replaceWith(l);
        }
    }
};

function onAddResource(elem, placeholder='resource name', editing=false, uuid=null, url=null){
    var i = onAddResourceNewInput(placeholder, editing, uuid, url);
    elem.replaceWith(i);
    i.focus();
};





