document.addEventListener('DOMContentLoaded', function() {
	const selectElements = document.querySelectorAll('select');

	selectElements.forEach(selectElement => {
		selectElement.classList.add('select_search');
		selectElement.classList.add('form-select');
	});
});

// ロード時にイベントハンドラを仕掛ける
$(document).ready(function(){

    $('.select_search').select2({
		language: "ja" //日本語化
	});

    for (let i = 0; i < 17; i++) {
        $('#id_work_id-' + i + '-is_out').blur(calc_work_order);
        $('#id_work_id-' + i + '-count').blur(calc_work_order);
        $('#id_work_id-' + i + '-price').blur(calc_work_order);
    }
    $('#id_adjust').blur(calc_work_order);

    calc_work_order();

    const inputElements = document.querySelectorAll('input[type="text"], input[type="number"], input[type="date"]');
	inputElements.forEach(inputElement => {
		inputElement.classList.add('form-control');
	});
});

/**
 * 伝票金額計算する
 */
function calc_work_order() {
    // 明細行の金額算出と足しこみ
    let g_total = 0;
    for (let i = 0; i < 17; i++) {
        // 伝票出力対象かどうかチェック
        if (!$('#id_work_id-' + i + '-is_out').prop("checked")) continue;
        const row_total = Number($('#id_work_id-' + i + '-count').val()) * Number($('#id_work_id-' + i + '-price').val());
        g_total = g_total + row_total;
        $('#id_work_id-' + i + '-total').val(row_total);
    }
    $('#id_sum').val(g_total);
    // 最終的な金額を算出する
    $('#id_total').val(
        Math.round((Number($('#id_sum').val()) + Number($('#id_adjust').val())) * 1.1)
    );
}