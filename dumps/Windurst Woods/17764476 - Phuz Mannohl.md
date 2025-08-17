# 17764476 - Phuz Mannohl

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 192 bytes                |
| Total Events     | 17                       |
| References Count | 4                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [65535.3](#event-655353) | 0x001A       |      9 |              3 |
| [344](#event-344)        | 0x0023       |     33 |             12 |
| [523](#event-523)        | 0x0044       |      1 |              1 |
| [527](#event-527)        | 0x0045       |      3 |              2 |
| [535](#event-535)        | 0x0048       |      3 |              2 |
| [537](#event-537)        | 0x004B       |      3 |              2 |
| [531](#event-531)        | 0x004E       |      3 |              2 |
| [541](#event-541)        | 0x0051       |      3 |              2 |
| [546](#event-546)        | 0x0054       |      3 |              2 |
| [351](#event-351)        | 0x0057       |      1 |              1 |
| [357](#event-357)        | 0x0058       |      1 |              1 |
| [661](#event-661)        | 0x0059       |      1 |              1 |
| [664](#event-664)        | 0x005A       |      1 |              1 |
| [666](#event-666)        | 0x005B       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0050      |          80 |
|       1 | 0x001E      |          30 |
|       2 | 0x2046      |        8262 |
|       3 | 0x2047      |        8263 |

## String References

- **8262**: Wanna know why the chieftainness keeps herrr eyes closed all the time?
- **8263**: It's so she can hearrr the voice of naturrre betterrr!

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=80*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0011 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0016 [0x1C] WAIT(30* ticks)
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001A  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                5E 69 64 6C 30 1C            ^idl0.
0020: 01 80 00                                          ...             
```

#### Opcodes

```
  0: 0x001A [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x001F [0x1C] WAIT(30* ticks)
  2: 0x0022 [0x00] END_REQSTACK()
```

### Event 344

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          1E F0 FF FF 7F  6F 70 29 08 7C 10 0F 01     .....op).|...
0030: 01 1D 02 80 23 1D 03 80  23 29 08 7C 10 0F 01 02  ....#...#).|....
0040: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0023 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0028 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0029 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x002A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Phuz Mannohl (ID: 17764476/0x010F107C), tag_num=0x01)
  4: 0x0031 [0x1D] PRINT_EVENT_MESSAGE(message_id=8262*)
    → "Wanna know why the chieftainness keeps herrr eyes closed all the time?"
  5: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=8263*)
    → "It's so she can hearrr the voice of naturrre betterrr!"
  7: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0039 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Phuz Mannohl (ID: 17764476/0x010F107C), tag_num=0x02)
  9: 0x0040 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0042 [0x21] END_EVENT
 11: 0x0043 [0x00] END_REQSTACK()
```

### Event 523

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             00                                        .           
```

#### Opcodes

```
  0: 0x0044 [0x00] END_REQSTACK()
```

### Event 527

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0045  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                22 01 00                                "..        
```

#### Opcodes

```
  0: 0x0045 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0047 [0x00] END_REQSTACK()
```

### Event 535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0048  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          22 01 00                         "..     
```

#### Opcodes

```
  0: 0x0048 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x004A [0x00] END_REQSTACK()
```

### Event 537

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004B  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   22 01 00                   "..  
```

#### Opcodes

```
  0: 0x004B [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x004D [0x00] END_REQSTACK()
```

### Event 531

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004E  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            22 01                ".
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x004E [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0050 [0x00] END_REQSTACK()
```

### Event 541

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0051  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    22 01 00                                        "..            
```

#### Opcodes

```
  0: 0x0051 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0053 [0x00] END_REQSTACK()
```

### Event 546

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0054  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             22 01 00                                  "..         
```

#### Opcodes

```
  0: 0x0054 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0056 [0x00] END_REQSTACK()
```

### Event 351

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0057  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      00                                  .        
```

#### Opcodes

```
  0: 0x0057 [0x00] END_REQSTACK()
```

### Event 357

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0058  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          00                               .       
```

#### Opcodes

```
  0: 0x0058 [0x00] END_REQSTACK()
```

### Event 661

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0059  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             00                             .      
```

#### Opcodes

```
  0: 0x0059 [0x00] END_REQSTACK()
```

### Event 664

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                00                           .     
```

#### Opcodes

```
  0: 0x005A [0x00] END_REQSTACK()
```

### Event 666

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   00                         .    
```

#### Opcodes

```
  0: 0x005B [0x00] END_REQSTACK()
```
