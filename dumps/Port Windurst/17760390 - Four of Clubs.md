# 17760390 - Four of Clubs

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 72 bytes                |
| Total Events     | 4                       |
| References Count | 3                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      1 |              1 |
| [65535.2](#event-655352) | 0x0002       |      4 |              2 |
| [218](#event-218)        | 0x0006       |     19 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0E30      |        3632 |
|       2 | 0x0E31      |        3633 |

## String References

- **3632**: wIn-DuRSt$26WAt-ErS$26iS ThRoUgH$26tHIs$26ArCh!
- **3633**: In$26wIn-DuRSt$26WAt-ErS$26tHeRe$26Is$26tHe$26oPTi-STerY,$26RhInO-sTeRY,$26aNd$26AUrA-sTErY!

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
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1C 00 80 00                                   ....          
```

#### Opcodes

```
  0: 0x0002 [0x1C] WAIT(30* ticks)
  1: 0x0005 [0x00] END_REQSTACK()
```

### Event 218

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0006   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   1E F0  FF FF 7F 6F 70 1D 01 80        .....op...
0010: 23 1D 02 80 23 20 00 21  00                       #...# .!.       
```

#### Opcodes

```
  0: 0x0006 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x000B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x000C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x000D [0x1D] PRINT_EVENT_MESSAGE(message_id=3632*)
    → "wIn-DuRSt$26WAt-ErS$26iS ThRoUgH$26tHIs$26ArCh!"
  4: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=3633*)
    → "In$26wIn-DuRSt$26WAt-ErS$26tHeRe$26Is$26tHe$26oPTi-STerY,$26RhInO-sTeRY,$26aNd$26AUrA-sTErY!"
  6: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0015 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0017 [0x21] END_EVENT
  9: 0x0018 [0x00] END_REQSTACK()
```
