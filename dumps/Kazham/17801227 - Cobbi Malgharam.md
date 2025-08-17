# 17801227 - Cobbi Malgharam

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 148 bytes        |
| Total Events     | 8                |
| References Count | 8                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [41](#event-41)          | 0x001A       |     15 |              8 |
| [161](#event-161)        | 0x0029       |     15 |              8 |
| [278](#event-278)        | 0x0038       |      1 |              1 |
| [293](#event-293)        | 0x0039       |      1 |              1 |
| [65535.3](#event-655353) | 0x003A       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x26EF      |        9967 |
|       3 | 0x285C      |       10332 |
|       4 | 0x16283     |       90755 |
|       5 | 0xFFFE429A  |  4294853274 |
|       6 | 0xFFFFC75C  |  4294952796 |
|       7 | 0x0071      |         113 |

## String References

- **9967**: Move along. Move along. I don't care if you are an adventurerrr. We don't give special trrreatment to anyone.
- **10332**: Get out of here! We don't want to make the chieftainness any more uptight than she alrrready is!

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

### Event 41

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 15 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                1E F0 FF FF 7F 6F            .....o
0020: 70 1D 02 80 23 20 00 21  00                       p...# .!.       
```

#### Opcodes

```
  0: 0x001A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0020 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0021 [0x1D] PRINT_EVENT_MESSAGE(message_id=9967*)
    → "Move along. Move along. I don't care if you are an adventurerrr. We don't give special trrreatment to anyone."
  4: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0025 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  6: 0x0027 [0x21] END_EVENT
  7: 0x0028 [0x00] END_REQSTACK()
```

### Event 161

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 15 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             1E F0 FF FF 7F 6F 70           .....op
0030: 1D 03 80 23 20 00 21 00                           ...# .!.        
```

#### Opcodes

```
  0: 0x0029 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x002F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0030 [0x1D] PRINT_EVENT_MESSAGE(message_id=10332*)
    → "Get out of here! We don't want to make the chieftainness any more uptight than she alrrready is!"
  4: 0x0033 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0034 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  6: 0x0036 [0x21] END_EVENT
  7: 0x0037 [0x00] END_REQSTACK()
```

### Event 278

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0038  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          00                               .       
```

#### Opcodes

```
  0: 0x0038 [0x00] END_REQSTACK()
```

### Event 293

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0039  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             00                             .      
```

#### Opcodes

```
  0: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                37 04 80 05 80 06            7.....
0040: 80 07 80 00                                       ....            
```

#### Opcodes

```
  0: 0x003A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=90.755*, z=-114.022*, y=-14.500*, direction=9.9°*
  1: 0x0043 [0x00] END_REQSTACK()
```
