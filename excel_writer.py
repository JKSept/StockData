#WRITER TO XML
import pandas as pd
import requests
import xlsxwriter

from quantive_momentum import df

writer = pd.ExcelWriter('SP_500_sheet.xlsx', engine='xlsxwriter')
df.to_excel(writer, 'SP 500', index=False)

#set whole background and font colors
bg_color = '#def4f8'
font_color = '#252525'


#creating different formats to apply to columns
header_format = writer.book.add_format(
    {
        'bold': True,
        'font_size': 24,
        'font_name': 'Verdana',
        'font_color': font_color,
        'bg_color': bg_color,
        'border': 1,
        'align': 'center'
    }
)

string_format = writer.book.add_format(
    {
        'bold': True,
        'font_color': font_color,
        'bg_color': bg_color,
        'border': 1,
        'align': 'center'

    }
)

dollar_format = writer.book.add_format(
    {
        'num_format': '$0.00',
        'font_color': font_color,
        'bg_color': bg_color,
        'border': 1,
        'align': 'center'
    }
)

mcap_format = writer.book.add_format(
    {
        'num_format': '$#,##0',
        'font_color': font_color,
        'bg_color': bg_color,
        'border': 1,
        'align': 'center'
    }
)

int_format = writer.book.add_format(
    {
        'num_format': '0.00',
        'font_color': font_color,
        'bg_color': bg_color,
        'border': 1,
        'align': 'center'
    }
)


#creating a dictionary of columns and their formats
column_formats = {
    'A': ['Ticker', string_format],
    'B': ['Price', dollar_format],
    'C': ['Market Cap', mcap_format],
    'D': ['Change Percent', int_format]
}

#Looping through dictionary keys of the columns and their formats and writing them to the sheet
for column in column_formats.keys():
    writer.sheets['SP 500'].set_column(f'{column}:{column}', 50, column_formats[column][1])
    writer.sheets['SP 500'].write(f'{column}1', column_formats[column][0], header_format)

writer.save()