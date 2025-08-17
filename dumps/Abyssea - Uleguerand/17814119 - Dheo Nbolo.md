# 17814119 - Dheo Nbolo

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Abyssea - Uleguerand (ID: 253) |
| Block Size       | 92 bytes                       |
| Total Events     | 2                              |
| References Count | 4                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [346](#event-346)     | 0x0001       |     51 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003B      |          59 |
|       1 | 0x1F76      |        8054 |
|       2 | 0x1F77      |        8055 |
|       3 | 0x1F78      |        8056 |

## String References

- **8054**: Just one moment, strrranger. You're not from around these parts, are you? I'd recommend you speak to the conflux surveyor over there. If ya haven't alrrready, that is.
- **8055**: He can prrrovide ya with somethin' called visitant status that'll make life here in Abyssea a good deal easier for ya.
- **8056**: Why, without it, you'll have a harrrd enough time just convincing people to talk to you. Don't take it perrrsonally--if you'd been through a cataclysm, you'd be pretty wary of chattin' with strangers too, don't ya think?

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

### Event 346

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 51 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 67 D2 0F 01 67   .....opf..g...g
0010: D2 0F 01 74 6C 6B 30 1D  01 80 23 1D 02 80 23 1D  ...tlk0...#...#.
0020: 03 80 23 66 00 80 67 D2  0F 01 67 D2 0F 01 74 6C  ..#f..g...g...tl
0030: 6B 31 21 00                                       k1!.            
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Dheo Nbolo (ID: 17814119/0x010FD267), Dheo Nbolo (ID: 17814119/0x010FD267)], work=59*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=8054*)
    → "Just one moment, strrranger. You're not from around these parts, are you? I'd recommend you speak to the conflux surveyor over there. If ya haven't alrrready, that is."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=8055*)
    → "He can prrrovide ya with somethin' called visitant status that'll make life here in Abyssea a good deal easier for ya."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=8056*)
    → "Why, without it, you'll have a harrrd enough time just convincing people to talk to you. Don't take it perrrsonally--if you'd been through a cataclysm, you'd be pretty wary of chattin' with strangers too, don't ya think?"
  9: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0023 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Dheo Nbolo (ID: 17814119/0x010FD267), Dheo Nbolo (ID: 17814119/0x010FD267)], work=59*
 11: 0x0032 [0x21] END_EVENT
 12: 0x0033 [0x00] END_REQSTACK()
```
