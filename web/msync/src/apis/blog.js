import network from '@/assets/js/network';

export function publishBlog(params) {
  const url = '/v1/blog/publish';
  return network.post(url, params);
}

export function deleteBlog(params) {
  const url = '/v1/blog/publish';
  return network.delete(url, params);
}

export function fetchBlogContent(params) {
  const url = '/v1/blog/content';
  return network.post(url, params);
}

export function updateBlogContent(params) {
  const url = '/v1/blog/content';
  return network.put(url, params);
}

export function fetchBlogCate(params) {
  const url = '/v1/blog/cate';
  return network.post(url, params);
}

export function fetchBlogListInCate(params) {
  const url = '/v1/blog/list';
  return network.post(url, params);
}
