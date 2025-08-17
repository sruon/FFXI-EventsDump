# 17162721 - Ekki-Mokki

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 188 bytes                    |
| Total Events     | 5                            |
| References Count | 12                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [409](#event-409)        | 0x0001       |     60 |             10 |
| [231](#event-231)        | 0x003D       |      1 |              1 |
| [65535.1](#event-655351) | 0x003E       |     21 |              2 |
| [65535.2](#event-655352) | 0x0053       |     21 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0031      |          49 |
|       2 | 0x2AC8      |       10952 |
|       3 | 0x2AC9      |       10953 |
|       4 | 0x0005      |           5 |
|       5 | 0x0002      |           2 |
|       6 | 0x0000      |           0 |
|       7 | 0x0011      |          17 |
|       8 | 0x000E      |          14 |
|       9 | 0x0004      |           4 |
|      10 | 0x0006      |           6 |
|      11 | 0x00BE      |         190 |

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

### Event 409

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 60 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F8 FF FF 7F F0 FF  FF 7F 1C 00 80 66 01 80   J...........f..
0010: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 2B F8 FF FF  ........tlk0+...
0020: 7F 02 80 23 2B F8 FF FF  7F 03 80 23 66 01 80 F8  ...#+......#f...
0030: FF FF 7F F8 FF FF 7F 74  6C 6B 31 21 00           .......tlk1!.   
```

#### Opcodes

```
  0: 0x0001 [0x4A] EventEntity looks at LocalPlayer
  1: 0x000A [0x1C] WAIT(30* ticks)
  2: 0x000D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  3: 0x001C [0x2B] EventEntity [10952*]:
    → "They say this detestable Yagudo Theomilitary is led by one named Tzee Xicu the Manifest."
  4: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0024 [0x2B] EventEntity [10953*]:
    → "He marshals the throngs of Yagudo from the foul depths of Castle Oztroja. There are some rumors, however, that he is actually a she."
  6: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x002C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=49*
  8: 0x003B [0x21] END_EVENT
  9: 0x003C [0x00] END_REQSTACK()
```

### Event 231

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         00                     .  
```

#### Opcodes

```
  0: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            B6 0B                ..
0040: 04 80 05 80 06 80 07 80  06 80 08 80 09 80 06 80  ................
0050: 06 80 00                                          ...             
```

#### Opcodes

```
  0: 0x003E [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=2*, head=0*, body=17*, hands=0*, legs=14*, feet=4*, main=0*, sub=0*)
  1: 0x0052 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0053   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          B6 0B 04 80 05  80 0A 80 0A 80 0A 80 0A     .............
0060: 80 0A 80 0B 80 06 80 00                           ........        
```

#### Opcodes

```
  0: 0x0053 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=2*, head=6*, body=6*, hands=6*, legs=6*, feet=6*, main=190*, sub=0*)
  1: 0x0067 [0x00] END_REQSTACK()
```
