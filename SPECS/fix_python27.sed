s/%{__python}/python2.7/
s/python-/python27-/
s|%{python_sitelib}|/usr/lib/python2.7/site-packages|
s|%{python_archlib}|/usr/lib64/python2.7/site-packages|
s|?.?|2.7|
/rm -rf %{pypi_name}.egg-info/a find . -type f | xargs sed -i '/^#!/{s/python/python2.7/}'