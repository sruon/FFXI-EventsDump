# 17162739 - Khea Mhyyih

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 88 bytes                     |
| Total Events     | 3                            |
| References Count | 4                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [428](#event-428)     | 0x0001       |     42 |             10 |
| [32](#event-32)       | 0x002B       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x2AB0      |       10928 |
|       2 | 0x000C      |          12 |
|       3 | 0x2AB1      |       10929 |

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

### Event 428

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 42 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F8 FF FF 7F F0 FF  FF 7F 1C 00 80 2B F8 FF   J...........+..
0010: FF 7F 01 80 23 6E F8 FF  FF 7F 02 80 99 F8 FF FF  ....#n..........
0020: 7F 2B F8 FF FF 7F 03 80  23 21 00                 .+......#!.     
```

#### Opcodes

```
  0: 0x0001 [0x4A] EventEntity looks at LocalPlayer
  1: 0x000A [0x1C] WAIT(30* ticks)
  2: 0x000D [0x2B] EventEntity [10928*]:
    → "I am a member of the Wildcats, underrr the able command of General Haja Zhwan."
  3: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0015 [0x6E] EventEntity uses emote 12*
  5: 0x001C [0x99] Wait for EventEntity animation to complete
  6: 0x0021 [0x2B] EventEntity [10929*]:
    → "Have you ever seen her in action on the field of battle? Her crossbow never misses its tarrrget!"
  7: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0029 [0x21] END_EVENT
  9: 0x002A [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   00                         .    
```

#### Opcodes

```
  0: 0x002B [0x00] END_REQSTACK()
```
