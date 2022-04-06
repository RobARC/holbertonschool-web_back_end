export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') {
    return '';
  }
  const result = [...set]
    .map((x) => (typeof x === 'string' && x.startsWith(startString) ? x.slice(startString.length) : ''))
    .filter((x) => x !== '')
    .join('-');
  return result;
}
