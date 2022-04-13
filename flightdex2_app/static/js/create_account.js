function onChangeEmail(elem){
    if (elem.value != ''){
        postRequestAsync('email', elem);
    }
};

function onChangeOthersRequired(elem){
    if (elem.value == ''){
        elem.dataset.error = true;
    } else {
        elem.dataset.error = false;
        elem.style.outline = null;
    }
};

function onChangeStateSelection(selection, metros) {
    var selected = selection.value;
    var met = document.getElementById("metro");
    met.dataset.error = false;
    met.style.outline = null;

    while (met.firstChild) {
        met.removeChild(met.firstChild);
    }

    var opt;
    if (selected == ''){
        opt = document.createElement('option');
        opt.value = '';
        opt.innerHTML = 'Metro Area';
        met.appendChild(opt);
        selection.dataset.error = true;
    } else {
        for (var i=0; i < metros[selected].length; i++) {
            opt = document.createElement('option');
            opt.value = metros[selected][i];
            opt.innerHTML = metros[selected][i];
            met.appendChild(opt);
        }
        selection.dataset.error = false;
        selection.style.outline = null;
    }
};

function onChangeUsername(elem){
    if (elem.value != ''){
        postRequestAsync('username', elem);
    } else {
        elem.style.outline = null;
        elem.dataset.error = true;
    }
};


function onClickCreateAccount(){
    var error = false;
    var form = document.getElementById('create_account_form');
    var elements = form.querySelectorAll("[data-find='ca']");
    var elem;
    for (var i=0; i < elements.length; i++){
        elem = elements[i]
        if (elem.dataset.error == 'true' || (elem.value == '' && !['phone', 'company'].includes(elem.name))){
            elem.style.outline = 'solid 2px red';
            error = true;
        }
    }
    if (error) return;
    form.submit();
};

function onClickUserType(elem) {
    elem.dataset.error = false;
    var cousin;
    if (elem.id == 'd_client'){
        cousin = document.getElementById("d_pro");
    } else {
        cousin = document.getElementById("d_client");
    }
    cousin.checked= false;
    cousin.required=false;
    cousin.dataset.error = false;
};


function onInputEmail(elem){
    if (elem.value == ''){
        elem.style.outline = null;
        elem.dataset.error = true;
    }
    else if (elem.value.includes('.') && elem.value.includes('@')){
        var last_index_period = elem.value.lastIndexOf('.');
        if (last_index_period > elem.value.lastIndexOf('@') && last_index_period != elem.value.length - 1){
            elem.style.outline = null;
            elem.dataset.error = false;
        } else {
            elem.style.outline = 'solid 2px red';
            elem.dataset.error = true;
        }
    } else {
        elem.style.outline = 'solid 2px red';
        elem.dataset.error = true;
    }
};

function onInputPassword(elem){
    if (elem.value == ''){
        elem.style.outline = null;
        elem.dataset.error = true;
    }
    else if (elem.value.length < 8){
        elem.style.outline = 'solid 2px red';
        elem.dataset.error = true;
    } else {
        var hasChr = false;
        var hasNum = false;
        for (var i = 0; i < elem.value.length; i++){
            if (isNaN(parseInt(elem.value[i]))){
                hasChr = true;
            } else if (!isNaN(parseInt(elem.value[i]))){
                hasNum = true;
            }
        }
        if (hasChr && hasNum){
            elem.style.outline = null;
            elem.dataset.error = false;
        } else {
            elem.style.outline = 'solid 2px red';
            elem.dataset.error = true;
        }
    }
    var check = document.getElementById('password_confirm');
    if (check.value != ''){
        if (check.value != elem.value){
            check.style.outline = 'solid 2px red';
            check.dataset.error = true;
        } else {
            check.style.outline = null;
            check.dataset.error = false;
        }
    } else {
        check.dataset.error = true;
    }
};

function onInputPasswordConfirm(elem){
    var password = document.getElementById('password');
    if (elem.value == ''){
        elem.style.outline = null;
        elem.dataset.error = true;
    } else if (elem.value == password.value){
        elem.style.outline = null;
        elem.dataset.error = false;
    } else {
        elem.style.outline = 'solid 2px red';
        elem.dataset.error = true;
    }
};

function onInputPhone(elem){
    var val_without = elem.value.replaceAll('-', '').split('')
    val_without.splice(3, 0, '-');
    val_without.splice(7, 0, '-');
    elem.value = val_without.join('')
    var pos;
    if (val_without.length <= 4){
        pos = val_without.length - 2;
    } else if(val_without.length <= 8) {
        pos = val_without.length - 1;
    } else {
        pos = val_without.length;
    }
    elem.setSelectionRange(pos, pos);
};


function postRequestAsync(route_suffix, elem) {
    fetch(`${window.origin}/check_database_${route_suffix}`, {
        method: 'POST',
        credentials: 'include',
        body: JSON.stringify(elem.value),
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
                var resp = data[0];
                console.log(resp)
                if (!resp.valid){
                    elem.style.outline = 'solid 2px red';
                    elem.dataset.error = true;
                    elem.focus()
                    alert(`${resp.message}`)
                    return;
                } else {
                    elem.style.outline = null;
                    elem.dataset.error = false;
                    return;
                }
            })
        }
    })
};