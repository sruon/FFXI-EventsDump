# 17752210 - Eight of Hearts

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 96 bytes                  |
| Total Events     | 5                         |
| References Count | 3                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      1 |              1 |
| [65535.2](#event-655352) | 0x0002       |     22 |              4 |
| [65535.3](#event-655353) | 0x0018       |      4 |              2 |
| [276](#event-276)        | 0x001C       |     19 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x1F09      |        7945 |
|       2 | 0x1F0A      |        7946 |

## String References

- **7945**: ThIs$26Is WiNdUrSt$26WaTerS,$26oNe of$26tHe FoUr$26dIs-TrIcTs$26oF WiNdUrSt!
- **7946**: mOsT oF$26tHe TaRuTaRu$26liVe$26iN tHiS$26dIsTrIcT sO$26ThrEe$26oF tHe$26fIvE mIn-IsTrIeS$26aRe$26cEnTeReD hErE!

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

### Event 276

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      1E F0 FF FF              ....
0020: 7F 6F 70 1D 01 80 23 1D  02 80 23 20 00 21 00     .op...#...# .!. 
```

#### Opcodes

```
  0: 0x001C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0021 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0022 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0023 [0x1D] PRINT_EVENT_MESSAGE(message_id=7945*)
    → "ThIs$26Is WiNdUrSt$26WaTerS,$26oNe of$26tHe FoUr$26dIs-TrIcTs$26oF WiNdUrSt!"
  4: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0027 [0x1D] PRINT_EVENT_MESSAGE(message_id=7946*)
    → "mOsT oF$26tHe TaRuTaRu$26liVe$26iN tHiS$26dIsTrIcT sO$26ThrEe$26oF tHe$26fIvE mIn-IsTrIeS$26aRe$26cEnTeReD hErE!"
  6: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x002B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x002D [0x21] END_EVENT
  9: 0x002E [0x00] END_REQSTACK()
```
