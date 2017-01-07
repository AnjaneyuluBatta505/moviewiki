import random


def random_select(queryset):
	queryset = queryset.order_by("id")
	try:
		start = queryset.first().id
		end = queryset.last().id
		sample = []
		for i in range(0, 15):
			n = random.randint(start, end)
			sample.append(n)
		queryset = queryset.filter(id__in=set(sample))
		return queryset
	except:
		return []