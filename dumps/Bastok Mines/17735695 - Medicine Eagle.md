# 17735695 - Medicine Eagle

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Bastok Mines (ID: 234) |
| Block Size       | 156 bytes              |
| Total Events     | 8                      |
| References Count | 12                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |      1 |              1 |
| [25](#event-25)          | 0x0002       |     11 |              5 |
| [176](#event-176)        | 0x000D       |     15 |              3 |
| [181](#event-181)        | 0x001C       |     11 |              5 |
| [180](#event-180)        | 0x0027       |      1 |              1 |
| [65535.1](#event-655351) | 0x0028       |     10 |              2 |
| [65535.2](#event-655352) | 0x0032       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2936      |       10550 |
|       1 | 0xFFFDA261  |  4294812257 |
|       2 | 0xFFFF9CB8  |  4294941880 |
|       3 | 0x0000      |           0 |
|       4 | 0x05DA      |        1498 |
|       5 | 0x2D10      |       11536 |
|       6 | 0xFFFF7338  |  4294931256 |
|       7 | 0x7C09      |       31753 |
|       8 | 0x0243      |         579 |
|       9 | 0xFFFF6810  |  4294928400 |
|      10 | 0x9FA1      |       40865 |
|      11 | 0x04B9      |        1209 |

## String References

- **10550**: There's an inn and the Alchemists' Guild through here, but other than that, you'll only find the homes of Bastok's poor. I don't think there's anything you'd want in there.
- **11536**: And now there is talk of sending a party to investigate the Altepa Desert, but you should talk to Drake Fang in the Zeruhn Mines about that.

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

### Event 1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1E F0 FF FF 7F 1D  00 80 23 21 00             ........#!.   
```

#### Opcodes

```
  0: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0007 [0x1D] PRINT_EVENT_MESSAGE(message_id=10550*)
    → "There's an inn and the Alchemists' Guild through here, but other than that, you'll only find the homes of Bastok's poor. I don't think there's anything you'd want in there."
  2: 0x000A [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000B [0x21] END_EVENT
  4: 0x000C [0x00] END_REQSTACK()
```

### Event 176

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         37 01 80               7..
0010: 02 80 03 80 04 80 1E 0B  A0 0E 01 00              ............    
```

#### Opcodes

```
  0: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-155.039*, z=-25.416*, y=0.000*, direction=131.7°*
  1: 0x0016 [0x1E] EventEntity looks at Mydon (ID: 17735691/0x010EA00B) and starts talking
  2: 0x001B [0x00] END_REQSTACK()
```

### Event 181

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      1E F0 FF FF              ....
0020: 7F 1D 05 80 23 21 00                              ....#!.         
```

#### Opcodes

```
  0: 0x001C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0021 [0x1D] PRINT_EVENT_MESSAGE(message_id=11536*)
    → "And now there is talk of sending a party to investigate the Altepa Desert, but you should talk to Drake Fang in the Zeruhn Mines about that."
  2: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0025 [0x21] END_EVENT
  4: 0x0026 [0x00] END_REQSTACK()
```

### Event 180

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      00                                  .        
```

#### Opcodes

```
  0: 0x0027 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          37 06 80 07 80 03 80 08          7.......
0030: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0028 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-36.040*, z=31.753*, y=0.000*, direction=50.9°*
  1: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       37 09 80 0A 80 03  80 0B 80 00                7.........    
```

#### Opcodes

```
  0: 0x0032 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-38.896*, z=40.865*, y=0.000*, direction=106.3°*
  1: 0x003B [0x00] END_REQSTACK()
```
