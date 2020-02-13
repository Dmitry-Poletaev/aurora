
// Сортировка товара по цене
/*
document.querySelector('.acs_sorting_button').onclick = mySort;
document.querySelector('.desc_sorting_button').onclick = mySortDesc;

function mySort() {
    let list_item = document.querySelector('.product-list');
    for (let i = 0; i < list_item.children.length; i++ ) {
        for (let j = i; j < list_item.length; j++) {
            if (+list_item.children[i].getAtribute('data-price') > +list_item.children[j].getAtribute('data-price')) {
                replacedNode = list_item.replaceChild(list_item.children[j], list_item.children[i]);
                insertAfter(replacedNode, list_item.children[i]);
            }
        }
    }

}

function mySortDesc() {
    let list_item = document.querySelector('.product-list');
    for (let i = 0; i < list_item.children.length; i++ ) {
        for (let j = i; j < list_item.length; j++) {
            if (+list_item.children[i].getAtribute('data-price') < +list_item.children[j].getAtribute('data-price')) {
                replacedNode = list_item.replaceChild(list_item.children[j], list_item.children[i]);
                insertAfter(replacedNode, list_item.children[i]);
            }
        }
    }

}

function insertAfter(elem, refElem){
    return refElem.parentNode.insertBefore(elem, refElem.nextSibling);
} */


$(function() {

    let sortingMethod = $(this).val();

    if(sortingMethod == '.asc_sorting_button')
    {
        sortProductsPriceAscending();
    }
    else if(sortingMethod == '.desc_sorting_button')
    {
        sortProductsPriceDescending();
    }

});
function sortProductsPriceAscending()
{
    let products = $('.product-price');
    products.sort(function(a, b){ return $(a).data("sort")-$(b).data("sort")});
    $(".product-list").html(products);

}

function sortProductsPriceDescending()
{
    let products = $('.product-price');
    products.sort(function(a, b){ return $(b).data("sort") - $(a).data("sort")});
    $(".product-list").html(products);

}