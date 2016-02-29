/**
 * Created by Jason Cozens on 13/01/2016.
 */
(function () {
    var $inputs;
    $inputs = $('[placeholder]');
    $inputs.each(function (i, t) {
        var $target, placeholder, text;
        $target = $(t);
        text = $target.attr('placeholder');
        placeholder = $('<span class="placeholder" />').text(text);
        return $target.attr('placeholder', null).after(placeholder);
    }).on('change', function () {
        var $target, hasValue;
        $target = $(this);
        hasValue = $target.val().length > 0;
        return $target.toggleClass('has-value', hasValue);
    });
}.call(this));(function () {
    var $inputs;
    $inputs = $('[placeholder]');
    $inputs.each(function (i, t) {
        var $target, placeholder, text;
        $target = $(t);
        text = $target.attr('placeholder');
        placeholder = $('<span class="placeholder" />').text(text);
        return $target.attr('placeholder', null).after(placeholder);
    }).on('change', function () {
        var $target, hasValue;
        $target = $(this);
        hasValue = $target.val().length > 0;
        return $target.toggleClass('has-value', hasValue);
    });
}.call(this));
