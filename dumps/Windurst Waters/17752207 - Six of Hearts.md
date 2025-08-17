# 17752207 - Six of Hearts

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 88 bytes                  |
| Total Events     | 5                         |
| References Count | 2                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      1 |              1 |
| [65535.2](#event-655352) | 0x0002       |     22 |              4 |
| [65535.3](#event-655353) | 0x0018       |      4 |              2 |
| [274](#event-274)        | 0x001C       |     15 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x1F06      |        7942 |

## String References

- **7942**: aLL$26rOaDs$26LEad$26TO tHe$26GReAt$26sTAr$26tREe!$26THiS ROad$26aL-So$26LEadS$26To tHe$26GrEaT$26StaR$26TreE!

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       53 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 5E    S........tlk0^
0010: 69 64 6C 30 1C 00 80 00                           idl0....        
```

#### Opcodes

```
  0: 0x0002 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x000F [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0014 [0x1C] WAIT(30* ticks)
  3: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0018  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          1C 00 80 00                      ....    
```

#### Opcodes

```
  0: 0x0018 [0x1C] WAIT(30* ticks)
  1: 0x001B [0x00] END_REQSTACK()
```

### Event 274

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 15 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      1E F0 FF FF              ....
0020: 7F 6F 70 1D 01 80 23 20  00 21 00                 .op...# .!.     
```

#### Opcodes

```
  0: 0x001C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0021 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0022 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0023 [0x1D] PRINT_EVENT_MESSAGE(message_id=7942*)
    → "aLL$26rOaDs$26LEad$26TO tHe$26GReAt$26sTAr$26tREe!$26THiS ROad$26aL-So$26LEadS$26To tHe$26GrEaT$26StaR$26TreE!"
  4: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0027 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  6: 0x0029 [0x21] END_EVENT
  7: 0x002A [0x00] END_REQSTACK()
```
