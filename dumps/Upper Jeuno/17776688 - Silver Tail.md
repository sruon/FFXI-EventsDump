# 17776688 - Silver Tail

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 168 bytes             |
| Total Events     | 12                    |
| References Count | 4                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [17](#event-17)       | 0x0001       |      1 |              1 |
| [13](#event-13)       | 0x0002       |      1 |              1 |
| [12](#event-12)       | 0x0003       |      1 |              1 |
| [67](#event-67)       | 0x0004       |     75 |             17 |
| [10015](#event-10015) | 0x004F       |      1 |              1 |
| [10221](#event-10221) | 0x0050       |      1 |              1 |
| [10230](#event-10230) | 0x0051       |      1 |              1 |
| [10231](#event-10231) | 0x0052       |      1 |              1 |
| [10232](#event-10232) | 0x0053       |      1 |              1 |
| [10233](#event-10233) | 0x0054       |      1 |              1 |
| [10234](#event-10234) | 0x0055       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003C      |          60 |
|       1 | 0x1DC7      |        7623 |
|       2 | 0x001E      |          30 |
|       3 | 0x1DC8      |        7624 |

## String References

- **7623**: The master of this chocobo stable is famous! It is an honor to ride a bird here.
- **7624**: I want to have one of the chocobos for my own, but the master's stubborn! I wonder if he'll ever say yes.

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

### Event 17

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

### Event 13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 67

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 75 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             1E F0 FF FF  7F 6F 70 66 00 80 F8 FF      .....opf....
0010: FF 7F F8 FF FF 7F 74 6C  6B 30 1D 01 80 23 5E 69  ......tlk0...#^i
0020: 64 6C 30 1C 02 80 1E 0C  40 0F 01 6F 70 66 00 80  dl0.....@..opf..
0030: F8 FF FF 7F F8 FF FF 7F  64 69 73 30 1D 03 80 23  ........dis0...#
0040: 53 F8 FF FF 7F F8 FF FF  7F 64 69 73 30 21 00     S........dis0!. 
```

#### Opcodes

```
  0: 0x0004 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0009 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x000A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x000B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
  4: 0x001A [0x1D] PRINT_EVENT_MESSAGE(message_id=7623*)
    → "The master of this chocobo stable is famous! It is an honor to ride a bird here."
  5: 0x001D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x0023 [0x1C] WAIT(30* ticks)
  8: 0x0026 [0x1E] EventEntity looks at Brutus (ID: 17776652/0x010F400C) and starts talking
  9: 0x002B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 10: 0x002C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 11: 0x002D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=60*
 12: 0x003C [0x1D] PRINT_EVENT_MESSAGE(message_id=7624*)
    → "I want to have one of the chocobos for my own, but the master's stubborn! I wonder if he'll ever say yes."
 13: 0x003F [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0040 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
 15: 0x004D [0x21] END_EVENT
 16: 0x004E [0x00] END_REQSTACK()
```

### Event 10015

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               00                 .
```

#### Opcodes

```
  0: 0x004F [0x00] END_REQSTACK()
```

### Event 10221

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

### Event 10230

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0051  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    00                                              .              
```

#### Opcodes

```
  0: 0x0051 [0x00] END_REQSTACK()
```

### Event 10231

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0052  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       00                                            .             
```

#### Opcodes

```
  0: 0x0052 [0x00] END_REQSTACK()
```

### Event 10232

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0053  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          00                                          .            
```

#### Opcodes

```
  0: 0x0053 [0x00] END_REQSTACK()
```

### Event 10233

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0054  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             00                                        .           
```

#### Opcodes

```
  0: 0x0054 [0x00] END_REQSTACK()
```

### Event 10234

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0055  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                00                                      .          
```

#### Opcodes

```
  0: 0x0055 [0x00] END_REQSTACK()
```
