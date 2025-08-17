# 16982293 - Ahkk Jharcham

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 180 bytes                     |
| Total Events     | 8                             |
| References Count | 6                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [9](#event-9)         | 0x0001       |      1 |              1 |
| [10](#event-10)       | 0x0002       |     53 |              9 |
| [11](#event-11)       | 0x0037       |      1 |              1 |
| [12](#event-12)       | 0x0038       |     10 |              4 |
| [13](#event-13)       | 0x0042       |     24 |              8 |
| [14](#event-14)       | 0x005A       |     17 |              7 |
| [3097](#event-3097)   | 0x006B       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0054      |          84 |
|       1 | 0x15B8      |        5560 |
|       2 | 0x001E      |          30 |
|       3 | 0x15B1      |        5553 |
|       4 | 0x15C7      |        5575 |
|       5 | 0x15C6      |        5574 |

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

### Event 9

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

### Event 10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 53 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       42 81 00 15 21 03  01 5B 00 80 15 21 03 01    B...!..[...!..
0010: 15 21 03 01 6B 69 73 69  2B 15 21 03 01 01 80 1C  .!..kisi+.!.....
0020: 02 80 53 15 21 03 01 15  21 03 01 6B 69 73 69 81  ..S.!...!..kisi.
0030: 01 15 21 03 01 21 00                              ..!..!.         
```

#### Opcodes

```
  0: 0x0002 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0003 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=Ahkk Jharcham (ID: 16982293/0x01032115))
  2: 0x0009 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kisi" with entities [Ahkk Jharcham (ID: 16982293/0x01032115), Ahkk Jharcham (ID: 16982293/0x01032115)], work=84*
  3: 0x0018 [0x2B] Ahkk Jharcham (ID: 16982293/0x01032115) [5560*]:
    → "Myehehe...\u0000\u0007"
  4: 0x001F [0x1C] WAIT(30* ticks)
  5: 0x0022 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kisi" with entities [Ahkk Jharcham (ID: 16982293/0x01032115), Ahkk Jharcham (ID: 16982293/0x01032115)]
  6: 0x002F [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=Ahkk Jharcham (ID: 16982293/0x01032115))
  7: 0x0035 [0x21] END_EVENT
  8: 0x0036 [0x00] END_REQSTACK()
```

### Event 11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0037  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      00                                  .        
```

#### Opcodes

```
  0: 0x0037 [0x00] END_REQSTACK()
```

### Event 12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 10 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          2B 15 21 03 01 03 80 23          +.!....#
0040: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0038 [0x2B] Ahkk Jharcham (ID: 16982293/0x01032115) [5553*]:
    → "Mew mew mew mew mew meooow\u0001t Tulutululu\u0001`\u0001t Meow!\u007F1\u0000\u0007"
  1: 0x003F [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0040 [0x21] END_EVENT
  3: 0x0041 [0x00] END_REQSTACK()
```

### Event 13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 24 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       1E F0 FF FF 7F 6F  70 29 10 F0 FF FF 7F 1D    .....op)......
0050: 2B 15 21 03 01 04 80 23  21 00                    +.!....#!.      
```

#### Opcodes

```
  0: 0x0042 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0047 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0048 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0049 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x1D)
  4: 0x0050 [0x2B] Ahkk Jharcham (ID: 16982293/0x01032115) [5575*]:
    → "Thanks, but I don't need any morrre parchment. Oh well, it's the thought that counts! (At least, that's what Mom always says...)\u007F1\u0000\u0007"
  5: 0x0057 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0058 [0x21] END_EVENT
  7: 0x0059 [0x00] END_REQSTACK()
```

### Event 14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 17 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                1E F0 FF FF 7F 6F            .....o
0060: 70 2B 15 21 03 01 05 80  23 21 00                 p+.!....#!.     
```

#### Opcodes

```
  0: 0x005A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x005F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0060 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0061 [0x2B] Ahkk Jharcham (ID: 16982293/0x01032115) [5574*]:
    → "Meow? You want to give me something? Unforrrtunately, I'm not cheap! (At least, that's what Mom always says...)\u007F1\u0000\u0007"
  4: 0x0068 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0069 [0x21] END_EVENT
  6: 0x006A [0x00] END_REQSTACK()
```

### Event 3097

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   00                         .    
```

#### Opcodes

```
  0: 0x006B [0x00] END_REQSTACK()
```
