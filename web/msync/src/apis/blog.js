import network from '@/assets/js/network';

export function publishBlog(params) {
  const url = '/v1/blog/publish';
  return network.post(url, params);
}

export function deleteBlog(params) {
  const url = '/v1/blog/delete';
  return network.delete(url, params);
}

export function fetchBlog(params) {
  const url = '/v1/blog/fetch';
  return network.post(url, params);
}

export function updateBlog(params) {
  const url = '/v1/blog/update';
  return network.put(url, params);
}

export function fetchBlogCateList(params) {
  const url = '/v1/blog/cate_list';
  return network.post(url, params);
}

export function fetchBlogListInCate(params) {
  const url = '/v1/blog/list_in_cate';
  return network.post(url, params);
}
