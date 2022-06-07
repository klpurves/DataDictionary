'''Code to enable hiding single code blocks within a jupyter notebook.
This will ensure I can run notebook with confidential data in my local session without worrying that it will be visible in final output.
This approach should ensure I can share code on github without any potential identifying detail.

Used code snippets from https://gist.github.com/Zsailer/5d1f4e357c78409dd9a5a4e5c61be552,
Taken from https://stackoverflow.com/questions/31517194/how-to-hide-one-specific-cell-input-or-output-in-ipython-notebook'''



from IPython.core.display import display, HTML
toggle_code_str = '''
<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show Solution"></form>
'''

toggle_code_prepare_str = '''
    <script>
    function code_toggle() {
        if ($('div.cell.code_cell.rendered.selected div.input').css('display')!='none'){
            $('div.cell.code_cell.rendered.selected div.input').hide();
        } else {
            $('div.cell.code_cell.rendered.selected div.input').hide();
        }
    }
    </script>

'''

display(HTML(toggle_code_prepare_str + toggle_code_str))

def toggle_code():
    display(HTML(toggle_code_str))
