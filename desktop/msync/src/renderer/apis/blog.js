import network from '@/assets/js/network';

// 发布
export function publishBlog(params) {
  const url = '/v1/blog/publish';
  return network.post(url, params);
}

export function fetchBlogContent(params) {
  const url = '/v1/blog/content';
  return network.post(url, params);
}

export function fetchBlogCate(params) {
  const url = '/v1/blog/cate';
  return network.post(url, params);
}

export function fetchBlogList(params) {
  const url = '/v1/blog/list';
  return network.post(url, params);
}
