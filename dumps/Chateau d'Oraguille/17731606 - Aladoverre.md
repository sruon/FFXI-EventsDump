# 17731606 - Aladoverre

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Chateau d'Oraguille (ID: 233) |
| Block Size       | 116 bytes                     |
| Total Events     | 5                             |
| References Count | 7                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [9](#event-9)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     10 |              2 |
| [515](#event-515)        | 0x000C       |     36 |             10 |
| [596](#event-596)        | 0x0030       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0AD2      |        2770 |
|       1 | 0xFFFFF5FC  |  4294964732 |
|       2 | 0x0000      |           0 |
|       3 | 0x0837      |        2103 |
|       4 | 0x0014      |          20 |
|       5 | 0x1C3C      |        7228 |
|       6 | 0x001E      |          30 |

## String References

- **7228**: The dungeons lie below. If you're here to see a prisoner, make it quick.

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 00                7.........    
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=2.770*, z=-2.564*, y=0.000*, direction=184.8°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 515

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 36 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      1E F0 FF FF              ....
0010: 7F 6F 70 66 04 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  .opf..........tl
0020: 6B 30 1D 05 80 23 5E 69  64 6C 30 1C 06 80 21 00  k0...#^idl0...!.
```

#### Opcodes

```
  0: 0x000C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0011 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0012 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0013 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=7228*)
    → "The dungeons lie below. If you're here to see a prisoner, make it quick."
  5: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0026 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x002B [0x1C] WAIT(30* ticks)
  8: 0x002E [0x21] END_EVENT
  9: 0x002F [0x00] END_REQSTACK()
```

### Event 596

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0030  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0030 [0x00] END_REQSTACK()
```
