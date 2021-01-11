import network from '@/assets/js/network';

export function deleteBlog(params) {
  const url = '/v1/blog/delete';
  return network.delete(url, params);
}

export function fetchContent(params) {
  const url = '/v1/blog/fetch/content';
  return network.post(url, params);
}

export function publishUpdate(params) {
  const url = '/v1/blog/publish/update';
  return network.put(url, params);
}

export function publishNew(params) {
  const url = '/v1/blog/publish/new';
  return network.post(url, params);
}

export function fetchBlogCategoryList(params) {
  const url = '/v1/blog/list/category';
  return network.post(url, params);
}

export function fetchBlogList(params) {
  const url = '/v1/blog/list';
  return network.post(url, params);
}
