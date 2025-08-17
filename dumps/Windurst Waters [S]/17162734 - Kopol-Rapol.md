# 17162734 - Kopol-Rapol

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 120 bytes                    |
| Total Events     | 5                            |
| References Count | 5                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [422](#event-422)     | 0x0001       |     30 |              8 |
| [153](#event-153)     | 0x001F       |      1 |              1 |
| [224](#event-224)     | 0x0020       |     30 |              8 |
| [32](#event-32)       | 0x003E       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x2ADF      |       10975 |
|       2 | 0x2AE0      |       10976 |
|       3 | 0x2AF4      |       10996 |
|       4 | 0x2AF5      |       10997 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 422

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F8 FF FF 7F F0 FF  FF 7F 1C 00 80 2B F8 FF   J...........+..
0010: FF 7F 01 80 23 2B F8 FF  FF 7F 02 80 23 21 00     ....#+......#!. 
```

#### Opcodes

```
  0: 0x0001 [0x4A] EventEntity looks at LocalPlayer
  1: 0x000A [0x1C] WAIT(30* ticks)
  2: 0x000D [0x2B] EventEntity [10975*]:
    → "When I grow up, I'm gonna be the biggest Warlock Warlord ever!"
  3: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0015 [0x2B] EventEntity [10976*]:
    → "Do you know what a warlord is? I'm not quite sure...but it sure sounds really importantaru, right!?"
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x21] END_EVENT
  7: 0x001E [0x00] END_REQSTACK()
```

### Event 153

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               00                 .
```

#### Opcodes

```
  0: 0x001F [0x00] END_REQSTACK()
```

### Event 224

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 4A F8 FF FF 7F F0 FF FF  7F 1C 00 80 2B F8 FF FF  J...........+...
0030: 7F 03 80 23 2B F8 FF FF  7F 04 80 23 21 00        ...#+......#!.  
```

#### Opcodes

```
  0: 0x0020 [0x4A] EventEntity looks at LocalPlayer
  1: 0x0029 [0x1C] WAIT(30* ticks)
  2: 0x002C [0x2B] EventEntity [10996*]:
    → "My teachy-weacher says we need to "e-vac-u-a-taru.""
  3: 0x0033 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0034 [0x2B] EventEntity [10997*]:
    → "I don't know what that means, but it sure sounds fun!"
  5: 0x003B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x003C [0x21] END_EVENT
  7: 0x003D [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            00                   . 
```

#### Opcodes

```
  0: 0x003E [0x00] END_REQSTACK()
```
