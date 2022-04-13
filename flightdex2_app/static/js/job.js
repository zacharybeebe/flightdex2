
/*
function proOnClickCreateProposal(elem, pro_id, job){
    var div = document.getElementById('proposal_div');
    var p, label, input, ta, small, price;

    p = document.createElement('p');
    label = document.createElement('label');
    label.className = 'h6 m-1'
    if (job.project_price !== null) {
        label.innerHTML = 'Project Price Bid Amount';
        price = job.project_price
    } else {
        label.innerHTML = 'Hourly Price Bid Amount';
        price = job.hourly_price
    }

    input = document.createElement('input');
    input.type = 'number';
    input.className = 'form-input w-25';
    input.value = price;
    input.placeholder = 'Bid Amount';
    input.onchange = function(){proOnChangeInputBid(this)};
    input.dataset.error = false;


    p.appendChild(label);
    p.appendChild(document.createElement('br'));
    p.appendChild(input);
    p.appendChild(document.createElement('br'));
    div.appendChild(p);

    p = document.createElement('p');
    ta = document.createElement('textarea');
    ta.className = 'form-control w-66';
    ta.rows = 7;
    ta.placeholder = 'Proposal Description'
    ta.oninput = function(){proOnInputTaDescription(this)};
    ta.dataset.error = true;
    small = document.createElement('small')
    small.className = 'm-1';
    small.id = 'chr_count';
    small.innerHTML = '0 / 4096';

    p.appendChild(ta);
    p.appendChild(small);
    p.appendChild(document.createElement('br'));
    div.appendChild(p);

    elem.value = 'submit proposal'
    elem.onclick = function(){proOnClickSubmitProposal(input, ta, job.id, pro_id)}
    input.focus();
};


function proOnClickViewProposal(elem, proposal){
    var div = document.getElementById('proposal_div');
    var p, label, input, ta, small, price;

    p = document.createElement('p');
    label = document.createElement('label');
    label.className = 'h6 m-1'
    label.innerHTML = 'Bid Amount';

    input = document.createElement('input');
    input.type = 'number';
    input.className = 'form-input w-25';
    input.value = proposal.bid;
    input.placeholder = 'Bid Amount';
    input.onchange = function(){proOnChangeInputBid(this)};
    input.dataset.error = false;

    p.appendChild(label);
    p.appendChild(document.createElement('br'));
    p.appendChild(input);
    p.appendChild(document.createElement('br'));
    div.appendChild(p);

    p = document.createElement('p');
    ta = document.createElement('textarea');
    ta.className = 'form-control w-66';
    ta.rows = 7;
    ta.value = proposal.description;
    ta.placeholder = 'Proposal Description'
    ta.oninput = function(){proOnInputTaDescription(this)};
    ta.dataset.error = false;
    small = document.createElement('small')
    small.className = 'm-1';
    small.id = 'chr_count';
    small.innerHTML = `${proposal.description.length} / 4096`;

    p.appendChild(ta);
    p.appendChild(small);
    p.appendChild(document.createElement('br'));
    div.appendChild(p);

    elem.value = 'updated proposal'
    elem.onclick = function(){proOnClickUpdateProposal(input, ta, proposal.id)}
    input.focus();
};
*/

function proOnClickCreateProposal(elem, pro_id, job){
    var form = document.getElementById('proposal_submit_form');
    var p, label, input, ta, small, price;

    p = document.createElement('p');
    label = document.createElement('label');
    label.className = 'h6 m-1'
    if (job.project_price !== null) {
        label.innerHTML = 'Project Price Bid Amount';
        price = job.project_price
    } else {
        label.innerHTML = 'Hourly Price Bid Amount';
        price = job.hourly_price
    }

    input = document.createElement('input');
    input.type = 'number';
    input.className = 'form-input w-25';
    input.name = 'bid'
    input.value = price;
    input.placeholder = 'Bid Amount';
    input.onchange = function(){proOnChangeInputBid(this)};
    input.dataset.error = false;


    p.appendChild(label);
    p.appendChild(document.createElement('br'));
    p.appendChild(input);
    p.appendChild(document.createElement('br'));
    form.appendChild(p);

    p = document.createElement('p');
    ta = document.createElement('textarea');
    ta.className = 'form-control w-66';
    ta.name = 'description'
    ta.rows = 7;
    ta.placeholder = 'Proposal Description'
    ta.oninput = function(){proOnInputTaDescription(this)};
    ta.dataset.error = true;
    small = document.createElement('small')
    small.className = 'm-1';
    small.id = 'chr_count';
    small.innerHTML = '0 / 4096';

    p.appendChild(ta);
    p.appendChild(small);
    p.appendChild(document.createElement('br'));
    form.appendChild(p);

    elem.value = 'submit proposal'
    elem.onclick = function(){proOnClickSubmitProposal(input, ta)}
    input.focus();
};


function proOnClickViewProposal(elem, proposal){
    console.log('prop: ', proposal.id)
    var form = document.getElementById('proposal_update_form');
    var p, label, input, ta, small, price;

    p = document.createElement('p');
    label = document.createElement('label');
    label.className = 'h6 m-1'
    label.innerHTML = 'Bid Amount';

    input = document.createElement('input');
    input.type = 'number';
    input.className = 'form-input w-25';
    input.name = 'bid'
    input.value = proposal.bid;
    input.placeholder = 'Bid Amount';
    input.onchange = function(){proOnChangeInputBid(this)};
    input.dataset.error = false;

    p.appendChild(label);
    p.appendChild(document.createElement('br'));
    p.appendChild(input);
    p.appendChild(document.createElement('br'));
    form.appendChild(p);

    p = document.createElement('p');
    ta = document.createElement('textarea');
    ta.className = 'form-control w-66';
    ta.name = 'description'
    ta.rows = 7;
    ta.value = proposal.description;
    ta.placeholder = 'Proposal Description'
    ta.oninput = function(){proOnInputTaDescription(this)};
    ta.dataset.error = false;
    small = document.createElement('small')
    small.className = 'm-1';
    small.id = 'chr_count';
    small.innerHTML = `${proposal.description.length} / 4096`;

    p.appendChild(ta);
    p.appendChild(small);
    p.appendChild(document.createElement('br'));
    form.appendChild(p);

    elem.value = 'updated proposal'
    elem.onclick = function(){proOnClickUpdateProposal(input, ta)}
    input.focus();
};

function proOnClickSubmitProposal(bid_elem, description_elem){
    var error = false;
    if (bid_elem.dataset.error == 'true'){
        bid_elem.style.outline = 'solid red 2px';
        error = true;
    }
    if (description_elem.dataset.error == 'true'){
        description_elem.style.outline = 'solid red 2px';
        error = true;
    }
    if (error) return;
    document.getElementById('proposal_submit_form').submit()
};

function proOnClickUpdateProposal(bid_elem, description_elem){
    var error = false;
    if (bid_elem.dataset.error == 'true'){
        bid_elem.style.outline = 'solid red 2px';
        error = true;
    }
    if (description_elem.dataset.error == 'true'){
        description_elem.style.outline = 'solid red 2px';
        error = true;
    }
    if (error) return;
    document.getElementById('proposal_update_form').submit()
};

function proOnChangeInputBid(elem){
    if (parseFloat(elem.value) <= 0){
        elem.dataset.error = true;
        elem.style.outline = 'solid red 2px';
    } else {
        elem.dataset.error = false;
        elem.style.outline = null;
    }
};

function proOnInputTaDescription(elem){
    if (elem.value.length > 0){
        elem.dataset.error = false;
        elem.style.outline = null;
    } else {
        elem.dataset.error = true;
    }
    if (elem.value.length >= 4096){
        elem.value = elem.value.slice(0, 4096)
    }
    var small = document.getElementById('chr_count');
    small.innerHTML = `${elem.value.length} / 4096`
}