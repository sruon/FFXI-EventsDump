# 17764475 - Baha Mannohl

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
| [343](#event-343)        | 0x0023       |     33 |             12 |
| [527](#event-527)        | 0x0044       |      3 |              2 |
| [535](#event-535)        | 0x0047       |      3 |              2 |
| [537](#event-537)        | 0x004A       |      3 |              2 |
| [531](#event-531)        | 0x004D       |      3 |              2 |
| [523](#event-523)        | 0x0050       |      1 |              1 |
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
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x2044      |        8260 |
|       3 | 0x2045      |        8261 |

## String References

- **8260**: I brought my daughterrr here to meet the tribal chieftainness, and have herrr highness see just how the child is grrrowing.
- **8261**: The chieftainness inculcated my daughter on the Mithra spirit--the teachings of a people in harrrmony with naturrre. This is just as my motherrr had done forrr me.

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
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
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

### Event 343

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          1E F0 FF FF 7F  6F 70 29 08 7B 10 0F 01     .....op).{...
0030: 01 1D 02 80 23 1D 03 80  23 29 08 7B 10 0F 01 02  ....#...#).{....
0040: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0023 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0028 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0029 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x002A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Baha Mannohl (ID: 17764475/0x010F107B), tag_num=0x01)
  4: 0x0031 [0x1D] PRINT_EVENT_MESSAGE(message_id=8260*)
    → "I brought my daughterrr here to meet the tribal chieftainness, and have herrr highness see just how the child is grrrowing."
  5: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=8261*)
    → "The chieftainness inculcated my daughter on the Mithra spirit--the teachings of a people in harrrmony with naturrre. This is just as my motherrr had done forrr me."
  7: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0039 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Baha Mannohl (ID: 17764475/0x010F107B), tag_num=0x02)
  9: 0x0040 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0042 [0x21] END_EVENT
 11: 0x0043 [0x00] END_REQSTACK()
```

### Event 527

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             22 01 00                                  "..         
```

#### Opcodes

```
  0: 0x0044 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0046 [0x00] END_REQSTACK()
```

### Event 535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0047  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      22  01 00                           "..      
```

#### Opcodes

```
  0: 0x0047 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0049 [0x00] END_REQSTACK()
```

### Event 537

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004A  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                22 01 00                     "..   
```

#### Opcodes

```
  0: 0x004A [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x004C [0x00] END_REQSTACK()
```

### Event 531

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004D  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         22 01 00               "..
```

#### Opcodes

```
  0: 0x004D [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x004F [0x00] END_REQSTACK()
```

### Event 523

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0050  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0050 [0x00] END_REQSTACK()
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
