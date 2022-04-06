export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const int8view = new DataView(buffer);
  if (position < length) {
    int8view.setUint8(position, value);
  } else {
    throw Error('Position outside range');
  }
  return int8view;
}
