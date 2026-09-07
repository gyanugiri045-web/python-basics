#used letter template and replaced name and date.

letter ='''Dear <|name|>,
          you are selected!
          <|Date|>'''

print(letter.replace("<|name|>","Reyan").replace("<|Date|>","21 september 2026"))         #used (.replace) to replace 