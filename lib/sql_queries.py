
select_all_female_bears_return_name_and_age = """
SELECT
    name,
    age
FROM bears
WHERE sex = 'F';
"""


select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
SELECT
    name,
    age
FROM bears
WHERE alive = 1
ORDER BY age ASC;
"""


select_all_bears_younger_than_5_years_old = """
SELECT
    *
FROM bears
WHERE age < 5;
"""


select_all_bears_and_sort_by_age = """
SELECT
    *
FROM bears
ORDER BY age;
"""


select_bear_count_by_color = """
SELECT
    color,
    COUNT(*) AS bear_count
FROM bears
GROUP BY color;
"""


select_all_bears_names_and_orders_in_alphabetical_order = """
SELECT
    name
FROM bears
ORDER BY name ASC;
"""


select_oldest_bear_and_returns_name_and_age = """
SELECT
    name,
    age
FROM bears
ORDER BY age DESC
LIMIT 1;
"""


select_youngest_bear_and_returns_name_and_age = """
SELECT
    name,
    age
FROM bears
ORDER BY age ASC
LIMIT 1;
"""
