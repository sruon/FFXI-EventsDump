# 17764516 - Ten of Spades

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 92 bytes                 |
| Total Events     | 7                        |
| References Count | 3                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      1 |              1 |
| [65535.2](#event-655352) | 0x0002       |      9 |              3 |
| [265](#event-265)        | 0x000B       |     19 |             10 |
| [848](#event-848)        | 0x001E       |      1 |              1 |
| [871](#event-871)        | 0x001F       |      1 |              1 |
| [876](#event-876)        | 0x0020       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x1F5F      |        8031 |
|       2 | 0x1F60      |        8032 |

## String References

- **8031**: defInition$26Of "Equipment": Some-tHing That$26oNe eQuIps!
- **8032**: dO yOu$26haVe yOUr eQuipMent$26proPerly equiPped!?$26ReMemBer:$26There is A$26coRRect plAce fOr$26EveryThing!

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

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       5E 69 64 6C 30 1C  00 80 00                   ^idl0....     
```

#### Opcodes

```
  0: 0x0002 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0007 [0x1C] WAIT(30* ticks)
  2: 0x000A [0x00] END_REQSTACK()
```

### Event 265

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   1E F0 FF FF 7F             .....
0010: 6F 70 1D 01 80 23 1D 02  80 23 20 00 21 00        op...#...# .!.  
```

#### Opcodes

```
  0: 0x000B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0010 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0011 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0012 [0x1D] PRINT_EVENT_MESSAGE(message_id=8031*)
    → "defInition$26Of "Equipment": Some-tHing That$26oNe eQuIps!"
  4: 0x0015 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0016 [0x1D] PRINT_EVENT_MESSAGE(message_id=8032*)
    → "dO yOu$26haVe yOUr eQuipMent$26proPerly equiPped!?$26ReMemBer:$26There is A$26coRRect plAce fOr$26EveryThing!"
  6: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x001A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x001C [0x21] END_EVENT
  9: 0x001D [0x00] END_REQSTACK()
```

### Event 848

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            00                   . 
```

#### Opcodes

```
  0: 0x001E [0x00] END_REQSTACK()
```

### Event 871

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

### Event 876

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0020  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0020 [0x00] END_REQSTACK()
```
