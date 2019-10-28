# References:
# https://github.com/anibali/docker-pytorch/blob/master/cuda-10.0/Dockerfile
# https://github.com/pypa/pipenv/blob/master/Dockerfile

# Install from Base Lease Image
FROM kaiml/lease

# Install Jupyter Notebook Extensions
RUN jupyter contrib nbextension install --user \
    && jupyter nbextensions_configurator enable --user

# Install Jupyter Black
RUN jupyter nbextension install https://github.com/drillan/jupyter-black/archive/master.zip --user \
    && jupyter nbextension enable jupyter-black-master/jupyter-black

# Install Jupyter Isort
RUN jupyter nbextension install https://github.com/benjaminabel/jupyter-isort/archive/master.zip --user \
    && jupyter nbextension enable jupyter-isort-master/jupyter-isort

# # Install Jupyter Vim
RUN mkdir -p $(jupyter --data-dir)/nbextensions \
    && cd $(jupyter --data-dir)/nbextensions \ 
    && git clone https://github.com/lambdalisue/jupyter-vim-binding vim_binding \
    && chmod -R go-w vim_binding 
RUN jupyter nbextension enable vim_binding/vim_binding


## Enable Nbextensions (Reference URL: https://qiita.com/simonritchie/items/88161c806197a0b84174)

# Table Beautifier
RUN jupyter nbextension enable table_beautifier/main

# Table of Contents
RUN jupyter nbextension enable toc2/main

# Toggle all line numbers
RUN jupyter nbextension enable toggle_all_line_numbers/main

# AutoSaveTime
RUN jupyter nbextension enable autosavetime/main

# Collapsible Headings
RUN jupyter nbextension enable collapsible_headings/main

# Execute Time
RUN jupyter nbextension enable execute_time/ExecuteTime

# Codefolding
RUN jupyter nbextension enable codefolding/main

# Notify
RUN jupyter nbextension enable notify/notify

# Change Theme
RUN jt -t chesterish -T -f roboto -fs 9 -tf merriserif -tfs 11 -nf ptsans -nfs 11 -dfs 8 -ofs 8 \
    && sed -i '1s/^/.edit_mode .cell.selected .CodeMirror-focused:not(.cm-fat-cursor) { background-color: #1a0000 !important; }\n /' /root/.jupyter/custom/custom.css \
    && sed -i '1s/^/.edit_mode .cell.selected .CodeMirror-focused.cm-fat-cursor { background-color: #1a0000 !important; }\n /' /root/.jupyter/custom/custom.css

# Set Configuration Password
RUN jupyter notebook --generate-config