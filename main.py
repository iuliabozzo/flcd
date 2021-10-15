from domain.symbol_table import SymbolTable

st = SymbolTable(10)
st.insert('ab')
st.insert('ba')
st.insert('5')
st.insert('12')
st.insert('asdf')
st.insert('asdf')
print(st)

print(st.contains('ab'))
print(st.lookup('asdfg'))