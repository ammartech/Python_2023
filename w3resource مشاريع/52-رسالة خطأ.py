import sys

print("هذه رسالة خطأ", file=sys.stderr)

sys.stderr.write("هذه رسألة خطأ أخري")
