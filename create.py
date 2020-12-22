from random import randint

def create_dummy():
	# return ""
	return f'asm("mov ${randint(0, 0xffffffff)}, %r10");'

flag = b"xm4s{mad_dummy_blocks_the_way!}"

code = """
#include<stdio.h>
int main(void) {
"""

for i in range(2000 + randint(0, 1000)):
	code += create_dummy()

code += f"int fail=0;"
code += f"printf(\"FLAG: \");"
code += f"char buf[{len(flag)+1}];"
for i in range(2000 + randint(0, 1000)):
	code += create_dummy()

code += f'scanf("%{len(flag)}s%*c", buf);'

for i in range(2000 + randint(0, 1000)):
	code += create_dummy()

for i, fi in enumerate(flag):
	code += f'if (buf[{i}] != {fi}) fail=1;'
	for i in range(2000 + randint(0, 1000)):
		code += create_dummy()

code += """
if (fail) {
	puts("Incorrect...");
} else {
	puts("Correct!");
}
"""

code += "}"

print(code)
